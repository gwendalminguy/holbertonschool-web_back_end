#!/usr/bin/env python3
"""
exercice.py
"""
from functools import wraps
from typing import Union, Optional, Callable
from uuid import uuid4

import redis


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count calls.
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        Wrap method to count its calls.
        """
        self._redis.incr(method.__qualname__)

        return method(self, *args, **kwds)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to log a call history.
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        Wrap method to log its call history.
        """
        value = method(self, *args, **kwds)

        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        self._redis.rpush(f"{method.__qualname__}:outputs", str(value))

        return value

    return wrapper


def replay(fn: Callable) -> None:
    """
    ...
    """
    self = fn.__self__

    inputs = self._redis.lrange(f"{fn.__qualname__}:inputs", 0, -1)
    inputs = [e.decode("utf-8") for e in inputs]

    outputs = self._redis.lrange(f"{fn.__qualname__}:outputs", 0, -1)
    outputs = [e.decode("utf-8") for e in outputs]

    print(f"{fn.__qualname__} was called {len(inputs)} times:")

    for input, output in zip(inputs, outputs):
        print(f"{fn.__qualname__}(*{input}) -> {output}")


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

    @count_calls
    @call_history
    def store(
        self,
        data: Union[str, bytes, int, float]
    ) -> str:
        """
        Store data in the Redis cache.
        """
        key = str(uuid4())
        self._redis.set(key, data)

        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float, None]:
        """
        Get data from the Redis cache and eventually convert it.
        """
        value = self._redis.get(key)

        if value is not None and fn is not None:
            value = fn(value)

        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Get a string from the Redis cache and convert it.
        """
        value = self.get(
            key=key,
            fn=lambda data: data.decode("utf-8"),
        )

        return value

    def get_int(self, key: str) -> Optional[int]:
        """
        Get an integer from the Redis cache and convert it.
        """
        value = self.get(
            key=key,
            fn=lambda data: int(data),
        )

        return value
