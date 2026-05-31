#!/usr/bin/env python3
"""Module for executing multiple coroutines concurrently."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times concurrently and return delays in order.

    Args:
        n: Number of times to spawn wait_random
        max_delay: Maximum delay passed to each wait_random call

    Returns:
        List of delay floats in ascending order
    """
    delays: List[float] = []

    async def collect(coro):
        result = await coro
        inserted = False
        for i, val in enumerate(delays):
            if result < val:
                delays.insert(i, result)
                inserted = True
                break
        if not inserted:
            delays.append(result)

    await asyncio.gather(*[collect(wait_random(max_delay)) for _ in range(n)])
    return delays