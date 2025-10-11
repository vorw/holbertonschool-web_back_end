#!/usr/bin/env python3
"""Run n wait_random coroutines and return delays in ascending order."""


import asyncio
from typing import List
from 0_basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn n wait_random(max_delay) and return delays in completion order."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays

