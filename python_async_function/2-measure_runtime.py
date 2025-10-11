#!/usr/bin/env python3
"""Measure average execution time per coroutine for wait_n."""


import asyncio
import time
from typing import Union

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return total runtime / n for wait_n(n, max_delay)."""
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.perf_counter()
    total_time: float = end - start
    return total_time / n

