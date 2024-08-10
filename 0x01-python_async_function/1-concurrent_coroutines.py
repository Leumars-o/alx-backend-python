#!/usr/bin/env python3
"""This module executes multiple coroutines at the same time.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This coroutine will execute multiple coroutines at the same time with
    a specific delay.

    Args:
        n (int): The number of times the coroutine will be executed.
        max_delay (int): The maximum delay.

    Returns:
        float: The list of all the delays.
    """

    delays = [wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
