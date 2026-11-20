#!/usr/bin/env python3
"""
exercice.py
"""
from typing import Union, Optional, Callable
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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Get data from the Redis cache and eventually convert it.
        """
        value = self._redis.get(key)

        if fn is not None:
            value = fn(value)

        return value

    def get_str(self, key: str) -> Union[str, None]:
        """
        Get a string from the Redis cache and convert it.
        """
        value = self.get(
            key=key,
            fn=lambda data: data.decode("utf-8"),
        )

        return value

    def get_int(self, key: str) -> Union[int, None]:
        """
        Get an integer from the Redis cache and convert it.
        """
        value = self.get(
            key=key,
            fn=lambda data: int(data),
        )

        return value
