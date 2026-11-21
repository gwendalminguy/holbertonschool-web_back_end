#!/usr/bin/env python3
"""
web.py
"""
from functools import wraps
from typing import Callable

import redis
import requests

cache = redis.Redis(decode_responses=True)


def count_calls(fn: Callable) -> Callable:
    """
    Decorator to count calls.
    """
    @wraps(fn)
    def wrapper(url):
        """
        Wrap function to count its calls.
        """
        cache.incr(f"count:{url}")

        return fn(url)

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """
    Fetch a web page and cache its content for 10 seconds.
    """
    html = cache.get(name=url)

    if html is not None:
        return html

    response = requests.get(url)
    html = response.text

    cache.set(
        name=url,
        value=html,
        ex=10,
    )

    return html
