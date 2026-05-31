#!/usr/bin/env python3
"""Module for async comprehension collecting values from async_generator."""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random floats from async_generator using an async
    comprehension and return them as a list.
    """
    return [value async for value in async_generator()]
