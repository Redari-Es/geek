import aiohttp
import asyncio


async def hello(URL):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            response = await response.text()
            print((response))


if __name__ == "__main__":
    URL = 'http://python.org'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello(URL))
