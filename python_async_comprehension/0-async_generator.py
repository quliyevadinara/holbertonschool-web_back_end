#!/usr/bin/env python3
"""Module for async generator yielding random floats."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async coroutine that yields 10 random floats between 0 and 10,
    waiting 1 second asynchronously between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
