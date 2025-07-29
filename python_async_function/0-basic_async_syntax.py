#!/usr/bin/env python3
"""
0-basic_async_syntax.py
Module containing an asynchronous rcoroutine.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay.
    """
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
