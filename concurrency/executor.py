import time
from collections import deque
from concurrent.futures import Future, ThreadPoolExecutor, wait
from typing import Any, Callable, Generator, Iterable, TypeVar

T = TypeVar("T")
R = TypeVar("R")


def demo_executor() -> list[int]:
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(worker, i) for i in range(8)]
        results = [f.result() for f in futures]
    return results


def worker(n: int) -> int:
    time.sleep(0.1)
    return n * n


def demo_futures() -> list[int]:
    with ThreadPoolExecutor(max_workers=2) as ex:
        fs = [ex.submit(lambda x: x + 1, n) for n in range(5)]
        done, _ = wait(fs)
        return [f.result() for f in done]


def process_batch(items: list[T], batch_size: int = 10) -> Generator[T, None, None]:
    with ThreadPoolExecutor(max_workers=4) as ex:
        for i in range(0, len(items), batch_size):
            batch = items[i:i + batch_size]
            futures = [ex.submit(worker, item) for item in batch]  # type: ignore
            for f in futures:
                yield f.result()


def retry_with_backoff(fn: Callable[[], R], max_retries: int = 3, base_delay: float = 1.0) -> R:
    for attempt in range(max_retries):
        try:
            return fn()
        except Exception:
            if attempt == max_retries - 1:
                raise
            time.sleep(base_delay * (2 ** attempt))
    raise RuntimeError("unreachable")


class RateLimiter:
    """基于 deque 的滑动窗口限流，O(1) popleft。"""
    __slots__ = ("max_calls", "period", "timestamps")

    def __init__(self, max_calls: int, period: float = 1.0) -> None:
        self.max_calls = max_calls
        self.period = period
        self.timestamps: deque[float] = deque()

    def acquire(self) -> bool:
        now = time.time()
        window_start = now - self.period
        while self.timestamps and self.timestamps[0] < window_start:
            self.timestamps.popleft()
        
        if len(self.timestamps) >= self.max_calls:
            return False
        self.timestamps.append(now)
        return True


class TaskGroup:
    __slots__ = ("executor", "tasks")

    def __init__(self, max_workers: int = 4) -> None:
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.tasks: list[Future[Any]] = []

    def add(self, fn: Callable[..., Any], *args: Any) -> Future[Any]:
        fut = self.executor.submit(fn, *args)
        self.tasks.append(fut)
        return fut

    def results(self) -> list[Any]:
        return [t.result() for t in self.tasks]
