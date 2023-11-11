import asyncio
import aiohttp
import time 
import requests

async def fetch_url(url, session):
    async with session.get(url) as response:
        return await response.text()

async def main():
    url = "http://127.0.0.1:8000/get_image?q=an%20%20african%20with%20white%20beard%20"  # Replace with your actual URL
    num_requests = 2
    t1=time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(url, session) for _ in range(num_requests)]
        responses = await asyncio.gather(*tasks)


    t2=time.time()
    print(t2-t1,"ifnished")
def run1():
    url = "http://127.0.0.1:8000/get_image?q=an%20%20african%20with%20white%20beard%20" 
    response = requests.get(url)
    print(response.content[:100].hex())
    



asyncio.run(run1())
asyncio.run(run1())