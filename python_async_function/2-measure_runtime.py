#!/usr/bin/env python3
"""
2-measure_runtime.py
Module containing an asynchronous coroutine.
"""
import asyncio
import random
from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Executes wait_random n times.
    """
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()

    length: float = end - start

    return length / n
