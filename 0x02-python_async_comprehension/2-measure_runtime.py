#!/usr/bin/env python3
"""This module contains a function that handles runtime
    for 4 parallel comprehensions
"""

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This function measures the runtime of async_comprehension
    and returns the total runtime
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = asyncio.get_event_loop().time()
    return (end_time - start_time)
