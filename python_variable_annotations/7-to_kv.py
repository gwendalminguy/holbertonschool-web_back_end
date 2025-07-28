#!/usr/bin/env python3
"""
7-to_kv.py
Module containing function returning a tuple.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a string and squared int or float tuple.
    """
    square: float = v * v
    return (k, square)
