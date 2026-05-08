import asyncio
from typing import Any

import httpx


async def fetch_url(client: httpx.AsyncClient, url: str) -> int:
    resp = await client.get(url)
    resp.raise_for_status()
    return resp.status_code


async def batch_fetch(urls: list[str]) -> list[Any]:
    async with httpx.AsyncClient(http2=True, timeout=httpx.Timeout(30.0)) as client:
        tasks = [fetch_url(client, url) for url in urls]
        return await asyncio.gather(*tasks, return_exceptions=True)


async def main() -> None:
    urls = [
        "https://api.github.com",
        "https://httpbin.org/get",
    ]
    results = await batch_fetch(urls)
    for url, status in zip(urls, results):
        print(f"{url}: {status}")


if __name__ == "__main__":
    asyncio.run(main())
