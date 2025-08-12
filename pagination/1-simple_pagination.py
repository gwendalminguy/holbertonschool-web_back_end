#!/usr/bin/env python3
"""
0-simple_helper_function.py
Module containing the function index_range.
"""
import csv
import math
from typing import List


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Gets specific lines from a CSV file.
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        self.__dataset = self.dataset()

        start, end = index_range(page, page_size)
        results = []
        if start < len(self.__dataset) and end < len(self.__dataset):
            for i in range(end - start):
                results.append(self.__dataset[start + i + 1])
        return results


def index_range(page: int, page_size: int) -> tuple:
    """
    Finds the start index and the end index for pagination.
    """
    return ((page - 1) * page_size, page * page_size)
