#!/usr/bin/env python3
"""Module for measuring the runtime of wait_n."""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time per coroutine for wait_n.

    Args:
        n: Number of coroutines to run
        max_delay: Maximum delay passed to wait_n

    Returns:
        Average time per coroutine (total_time / n) as a float
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n
