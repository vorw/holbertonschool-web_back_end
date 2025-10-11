#!/usr/bin/env python3
"""Run many task_wait_random concurrently and return delays in order."""


import asyncio
from typing import List
from 3_tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn n task_wait_random with max_delay and return delays as they complete."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
