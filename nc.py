import asyncio
import sys


async def _stdin_readline():
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, sys.stdin.readline)


async def main():
    host, port = sys.argv[1:]
    reader, writer = await asyncio.open_connection(host, port)

    while True:
        line = await _stdin_readline()
        writer.write(line.encode())
        await writer.drain()


if __name__ == "__main__":
    asyncio.run(main())
