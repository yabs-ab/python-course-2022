r"""Async chat server/client.

The following text-based, utf-8 encoded, protocol should be
implemented:

client -> server:

    login <username>\n
    msg <msg>\n

server -> client:

    msg <username> <timestamp> <msg>\n

Messages should be broadcast to all connected clients!
"""

from __future__ import annotations
import asyncio
from contextlib import contextmanager
from dataclasses import dataclass
import re
import sys
import time
from typing import ClassVar, Generator, Pattern


HOST = "localhost"
PORT = 21213


@dataclass
class Login:
    """Login message."""

    RE: ClassVar[Pattern[bytes]] = re.compile(rb"login (\w+)\n")

    user: str

    @classmethod
    def from_client(cls, line: bytes) -> Login | None:
        """Construct `cls` from `line`."""
        match = cls.RE.match(line)

        if not match:
            return None

        (user,) = match.groups()

        try:
            return cls(user=user.decode())
        except UnicodeDecodeError:
            return None

    def to_bytes(self) -> bytes:
        """Return wire format."""
        return b"login %s\n" % (self.user.encode())


@dataclass
class Msg:
    """Message message."""

    SERVER_RE: ClassVar[Pattern[bytes]] = re.compile(rb"msg (.*)\n")
    CLIENT_RE: ClassVar[Pattern[bytes]] = re.compile(rb"msg (\w+) (\d+) (.*)\n")

    user: str
    timestamp: int
    text: str

    @classmethod
    def from_client(cls, user: str, line: bytes) -> Msg | None:
        """Construct `cls` from `user` and `line`."""
        match = cls.SERVER_RE.match(line)

        if not match:
            return None

        return cls(
            user=user,
            timestamp=int(time.time()),
            text=match.group(1).decode(errors="replace"),
        )

    @classmethod
    def from_server(cls, line: bytes) -> Msg | None:
        """Construct `cls` from `line`."""
        match = cls.CLIENT_RE.match(line)

        if not match:
            return None

        user, timestamp, text = match.groups()

        try:
            user = user.decode()
        except UnicodeDecodeError:
            return None

        return cls(
            user=user,
            timestamp=int(timestamp),
            text=text.decode(errors="replace"),
        )

    def to_bytes(self) -> bytes:
        """Return wire format."""
        return b"msg %s %d %s\n" % (
            self.user.encode(),
            self.timestamp,
            self.text.encode(),
        )


async def serve(host: str, port: int) -> None:
    """Serve chat server."""
    clients: list[asyncio.StreamWriter] = []

    @contextmanager
    def register_client(writer: asyncio.StreamWriter) -> Generator[None, None, None]:
        clients.append(writer)
        try:
            yield
        finally:
            clients.remove(writer)

    async def broadcast(msg: Msg) -> None:
        data = msg.to_bytes()

        for writer in clients:
            writer.write(data)

        await asyncio.gather(*(writer.drain() for writer in clients))

    # client connection callback
    async def connection_cb(
        reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ) -> None:
        # handle login
        login = Login.from_client(await reader.readline())

        if login is None:
            return

        # handle messages
        with register_client(writer):
            async for line in reader:
                msg = Msg.from_client(login.user, line)

                if msg is None:
                    break

                await broadcast(msg)

    # serve
    server = await asyncio.start_server(connection_cb, host, port)
    async with server:
        await server.serve_forever()


async def _stdin_readline() -> str:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, sys.stdin.readline)


async def connect(host: str, port: int, user: str) -> None:
    """Connect to chat server."""
    # make connection
    reader, writer = await asyncio.open_connection(host, port)

    # login
    writer.write(f"login {user}\n".encode())
    await writer.drain()

    # handlers
    async def handle_stdin() -> None:
        while True:
            line = await _stdin_readline()
            writer.write(f"msg {line}".encode())
            await writer.drain()

    async def handle_reader() -> None:
        async for line in reader:
            print(line.decode())

    await asyncio.gather(handle_stdin(), handle_reader())


async def main() -> None:
    """Program entry point."""
    # parse arguments
    prog = sys.argv.pop(0)

    try:
        sys.argv.remove("-s")
    except ValueError:
        client = True
    else:
        client = False

    if sys.argv:
        sys.exit(f"usage: {prog} [-s]")

    # start client or server
    if client:
        user = input("username: ")
        await connect(HOST, PORT, user)
    else:
        await serve(HOST, PORT)


if __name__ == "__main__":
    asyncio.run(main())
