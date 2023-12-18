import time
from concurrent.futures import ThreadPoolExecutor, wait


def demo_executor():
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(worker, i) for i in range(8)]
        results = [f.result() for f in futures]
    return results


def worker(n):
    time.sleep(0.1)
    return n * n


def demo_futures():
    with ThreadPoolExecutor(max_workers=2) as ex:
        fs = [ex.submit(lambda x: x + 1, n) for n in range(5)]
        done, _ = wait(fs)
        return [f.result() for f in done]


def process_batch(items, batch_size=10):
    with ThreadPoolExecutor(max_workers=4) as ex:
        for i in range(0, len(items), batch_size):
            batch = items[i:i + batch_size]
            futures = [ex.submit(worker, item) for item in batch]
            for f in futures:
                yield f.result()


def retry_with_backoff(fn, max_retries=3, base_delay=1):
    for attempt in range(max_retries):
        try:
            return fn()
        except Exception:
            if attempt == max_retries - 1:
                raise
            time.sleep(base_delay * (2 ** attempt))


class RateLimiter:
    def __init__(self, max_calls, period=1.0):
        self.max_calls = max_calls
        self.period = period
        self.timestamps = []

    def acquire(self):
        now = time.time()
        self.timestamps = [t for t in self.timestamps if now - t < self.period]
        if len(self.timestamps) >= self.max_calls:
            return False
        self.timestamps.append(now)
        return True


class TaskGroup:
    def __init__(self, max_workers=4):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.tasks = []

    def add(self, fn, *args):
        fut = self.executor.submit(fn, *args)
        self.tasks.append(fut)
        return fut

    def results(self):
        return [t.result() for t in self.tasks]
