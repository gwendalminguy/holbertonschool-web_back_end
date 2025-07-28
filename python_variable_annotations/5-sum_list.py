#!/usr/bin/env python3
"""
5-sum_list.py
Module containing function to compute the sum of a float list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Computes the sum of a float list.
    """
    sum: float = 0
    for num in input_list:
        sum += num
    return sum
