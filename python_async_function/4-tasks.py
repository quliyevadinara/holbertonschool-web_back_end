#!/usr/bin/env python3
"""Module for task_wait_n using asyncio.Task objects."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times and return delays in ascending order.

    Args:
        n: Number of tasks to spawn
        max_delay: Maximum delay passed to each task_wait_random call

    Returns:
        List of delay floats in ascending order
    """
    delays: List[float] = []

    async def collect(task):
        result = await task
        inserted = False
        for i, val in enumerate(delays):
            if result < val:
                delays.insert(i, result)
                inserted = True
                break
        if not inserted:
            delays.append(result)

    await asyncio.gather(*[collect(task_wait_random(max_delay))
                           for _ in range(n)])
    return delays