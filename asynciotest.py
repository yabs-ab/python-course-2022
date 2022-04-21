import asyncio
from itertools import count


async def connection_cb(reader, writer):
    while True:
        line = await reader.readline()
        print(line)


async def background_task():
    for c in count():
        print(c)
        await asyncio.sleep(1)


async def main():
    task = asyncio.create_task(background_task())

    server = await asyncio.start_server(connection_cb, "localhost", 9999)
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
