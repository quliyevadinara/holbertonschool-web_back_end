#!/usr/bin/env python3
"""Module for measuring runtime of four parallel async comprehensions."""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Run async_comprehension four times in parallel using asyncio.gather
    and return the total elapsed time.

    The runtime is ~10 seconds because all four coroutines run concurrently:
    each waits 1 second per yield × 10 yields = 10 seconds total, but since
    they overlap completely via asyncio.gather, the wall-clock time is still
    just ~10 seconds rather than ~40 seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    return time.perf_counter() - start
