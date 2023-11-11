import asyncio
import aiohttp
import time 

async def fetch_url(url, session):
    async with session.get(url) as response:
        return await response.text()

async def main():
    url = "http://127.0.0.1:8000/items/1?q=a%20astronut%20swimming%20in%20volcano"  # Replace with your actual URL
    num_requests = 10
    t1=time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(url, session) for _ in range(num_requests)]
        responses = await asyncio.gather(*tasks)


    t2=time.time()
    print(t2-t1,"ifnished")

asyncio.run(main())