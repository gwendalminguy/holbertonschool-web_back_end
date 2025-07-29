#!/usr/bin/env python3
"""
3-tasks.py
Module containing an asynchronous coroutine.
"""
import asyncio
import random
import time

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns a task.
    """
    task: asyncio.Task = asyncio.create_task(wait_random(max_delay))

    return task
