#!/usr/bin/env python3
"""This module contains the function that waits for a random time.

Returns:
    float: A random number between 0 and max_delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10):
    """A function that waits for a random time.

    Args:
        max_delay (int, optional): _description_. Defaults to 10.

    Returns:
        float: A random number between 0 and max_delay.
    """
    wait_random = random.uniform(0, max_delay)
    await asyncio.sleep(wait_random)
    return wait_random
