from aiohttp import ClientSession


async def get(url):
    async with ClientSession() as session:
        async with session.get(url=url) as response:
            return await response.json()


async def post(url, data):
    async with ClientSession() as session:
        async with session.post(url=url, json=data) as response:
            return await response.json()
