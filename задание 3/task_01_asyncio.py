import asyncio
import aiohttp
import time

# список url
urls = ['https://www.example.com'] * 10

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def async_fetch_all():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)

def async_execution():
    start_time = time.perf_counter()  # время старта
    asyncio.run(async_fetch_all())  # выполнение асинхронных задач
    end_time = time.perf_counter()  # время окончания
    print(f'processes time: {end_time - start_time:0.2f} seconds\n')

if __name__ == '__main__':
    async_execution()
