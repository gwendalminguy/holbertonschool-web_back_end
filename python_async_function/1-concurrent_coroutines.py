#!/usr/bin/env python3
"""
1-concurrent_coroutines.py
Module containing an asynchronous rcoroutine.
"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Executes wait_random n times.
    """
    delays = []
    for i in range(n):
        x = await wait_random(max_delay)
        j = 0
        for j in range(len(delays)):
            if delays[j] > x:
                break
        delays.insert(j, x)

    return delays
