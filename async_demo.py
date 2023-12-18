import asyncio
import httpx


async def fetch_url(client, url):
    resp = await client.get(url)
    return resp.status_code


async def batch_fetch(urls):
    async with httpx.AsyncClient(timeout=30) as client:
        tasks = [fetch_url(client, url) for url in urls]
        return await asyncio.gather(*tasks, return_exceptions=True)


async def main():
    urls = [
        "https://api.github.com",
        "https://httpbin.org/get",
    ]
    results = await batch_fetch(urls)
    for url, status in zip(urls, results):
        print(f"{url}: {status}")


if __name__ == "__main__":
    asyncio.run(main())
