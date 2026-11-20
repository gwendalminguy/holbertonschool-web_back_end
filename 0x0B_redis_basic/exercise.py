#!/usr/bin/env python3
"""
exercice.py
"""
from typing import Union
from uuid import uuid4

import redis


class Cache:
    """
    Simple Redis cache.
    """
    def __init__(self) -> None:
        """
        Initialize a Redis cache.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the Redis cache.
        """
        key = str(uuid4())
        self._redis.set(key, data)

        return key
