#!/usr/bin/env python3
"""Run many task_wait_random concurrently and collect delays."""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn n Task(wait_random) and return delays in completion order."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for coro in asyncio.as_completed(tasks):
        delays.append(await coro)
    return delays