#!/usr/bin/env python3
"""
0-simple_helper_function.py
Module containing the function index_range.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Finds the start index and the end index for pagination.
    """
    return ((page - 1) * page_size, page * page_size)
