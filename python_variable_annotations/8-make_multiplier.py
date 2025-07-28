#!/usr/bin/env python3
"""
8-make_multiplier.py
Module containing function returning a function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function multiplying a float by a given multiplier.
    """
    def function(n: float) -> float:
        return n * multiplier

    return function
