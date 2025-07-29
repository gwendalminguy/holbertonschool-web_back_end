#!/usr/bin/env python3
"""
1-concurrent_coroutines.py
Module containing an asynchronous rcoroutine.
"""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> float:
    """
    Executes wait_random n times.
    """
    delays = []
    for i in range(n):
        x = await wait_random(max_delay)
        delays.append(x)
        
    delays.sort()
    return delays