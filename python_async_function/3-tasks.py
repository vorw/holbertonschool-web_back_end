#!/usr/bin/env python3
"""Create an asyncio.Task from wait_random."""


import asyncio
from 0_basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return a Task for wait_random(max_delay)."""
    return asyncio.create_task(wait_random(max_delay))
