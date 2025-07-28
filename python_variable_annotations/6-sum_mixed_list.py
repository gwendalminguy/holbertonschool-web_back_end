#!/usr/bin/env python3
"""
6-sum_mixed_list.py
Module containing function to compute the sum of a float and int list.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Computes the sum of a float and int list.
    """
    sum: float = 0
    for num in mxd_lst:
        sum += num
    return sum
