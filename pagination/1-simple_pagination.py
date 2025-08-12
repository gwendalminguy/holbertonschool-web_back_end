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
        
        with open(self.DATA_FILE, 'r') as file:
            csv_file = csv.reader(file)
            start, end = index_range(page, page_size)
            rows = list(csv_file)
            if start + 1 < len(rows) and end + 1 < len(rows):
                results = []
                for i in range(end - start):
                    results.append(rows[start + i + 1])
                return results


def index_range(page: int, page_size: int) -> tuple:
    """
    Finds the start index and the end index for pagination.
    """
    return ((page - 1) * page_size, page * page_size)
