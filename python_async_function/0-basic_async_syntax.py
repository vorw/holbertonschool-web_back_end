#!/usr/bin/env python3
"""Async coroutine waiting random delay and returning it."""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait random delay ≤ max_delay and return it."""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay