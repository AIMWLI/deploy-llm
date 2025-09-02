import time
from functools import wraps


def timer(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = time.perf_counter() - start
        return result
    return wrapper


def chunk_list(items, size):
    for i in range(0, len(items), size):
        yield items[i:i + size]


def safe_get(d, *keys, default=None):
    for k in keys:
        try:
            d = d[k]
        except (KeyError, IndexError, TypeError):
            return default
    return d


class RetryConfig:
    def __init__(self, max_retries=3, delay=1, backoff=2):
        self.max_retries = max_retries
        self.delay = delay
        self.backoff = backoff
