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
import sys


HOST = "localhost"
PORT = 21213


@dataclass
class Login:
    """Login message."""


@dataclass
class Msg:
    """Message message."""


async def serve(host: str, port: int) -> None:
    """Serve chat server."""

    # client store
    clients = []

    @contextmanager
    def register(writer):
        clients.append(writer)
        try:
            yield
        finally:
            clients.remove(writer)

    # client connections
    async def connection_cb(reader, writer):
        with register(writer):
            while True:
                line = await reader.readline()

                if not line:
                    break

                for client in clients:
                    client.write(line)
                    await client.drain()

    # start server
    server = await asyncio.start_server(connection_cb, host, port)
    async with server:
        await server.serve_forever()


async def _stdin_readline():
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, sys.stdin.readline)


async def connect(host: str, port: int, user: str) -> None:
    """Connect to chat server."""
    reader, writer = await asyncio.open_connection(host, port)

    writer.write(b"login ")
    writer.write(user.encode())
    writer.write(b"\n")
    await writer.drain()

    async def handle_stdin():
        while True:
            line = await _stdin_readline()
            writer.write(line.encode())
            await writer.drain()

    async def handle_server_msg():
        while True:
            line = await reader.readline()
            print(line)

    await asyncio.gather(handle_stdin(), handle_server_msg())


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
