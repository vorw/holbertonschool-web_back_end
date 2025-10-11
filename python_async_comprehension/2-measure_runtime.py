#!/usr/bin/env python3
"""Measure runtime of running async_comprehension 4 times in parallel."""


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def _run_four() -> None:
    """Run async_comprehension 4 times concurrently."""
    await asyncio.gather(*(async_comprehension() for _ in range(4)))


def measure_runtime() -> float:
    """Return elapsed time to run four async_comprehensions."""
    start = time.perf_counter()
    asyncio.run(_run_four())
    end = time.perf_counter()
    return end - start
