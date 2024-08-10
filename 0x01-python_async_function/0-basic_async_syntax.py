#!/usr/bin/env python3
"""This module contains the function that waits for a random time.

Returns:
    float: A random number between 0 and max_delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """A function that waits for a random time.

    Args:
        max_delay (int, optional): _description_. Defaults to 10.

    Returns:
        float: A random number between 0 and max_delay.
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
