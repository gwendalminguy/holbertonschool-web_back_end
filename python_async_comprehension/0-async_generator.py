#!/usr/bin/env python3
"""
0-async_generator.py
Module containing an asynchronous coroutine.
"""
import time
import random
from typing import List, Generator


async def async_generator() -> List[float]:
    """
    Waits for a 10 seconds and yields 10 numbers.
    """
    x: float
    for i in range(10):
        time.sleep(1)
        x = random.uniform(0, 10)
        yield(x)
