#!/usr/bin/env python3
"""This modoule measures the runtime of a function.
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """This function measures the runtime of a function.
    Args:
        n (int): The number of times the function will be called.
        max_delay (int): The maximum random float to wait.
    Returns:
        float: The average runtime.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
