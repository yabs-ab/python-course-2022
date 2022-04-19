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


async def connect(host: str, port: int, user: str) -> None:
    """Connect to chat server."""


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
