#!/usr/bin/env python3
"""
9-element_length.py
Module containing function returning a tuple list.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a tuple list.
    """
    return [(i, len(i)) for i in lst]
