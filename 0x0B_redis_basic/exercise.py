#!/usr/bin/env python3
"""
exercice.py
"""
from redis import Redis
from typing import Union
from uuid import uuid4


class Cache:
    """
    Simple Redis cache.
    """
    def __init__(self):
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the Redis cache.
        """
        key = str(uuid4())
        self._redis.set(key, data)

        return key
