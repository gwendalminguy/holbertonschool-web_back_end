#!/usr/bin/env python3
"""
4-tasks.py
Module containing an asynchronous coroutine.
"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Executes wait_random n times.
    """
    result: List[float] = []
    delays: List[float] = [
        asyncio.create_task(wait_random(max_delay)) for _ in range(n)
    ]

    for x in asyncio.as_completed(delays):
        y = await x
        result.append(y)

    return result
