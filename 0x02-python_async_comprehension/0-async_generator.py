#!/usr/bin/env python3
"""This module contains an Async Generator function
"""

import random
import asyncio


async def async_generator() -> float:
    """This function will generate a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
