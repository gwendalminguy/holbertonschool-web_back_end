#!/usr/bin/env python3
"""
3-hypermedia_del_pagination.py
Module containing deletion-resilient hypermedia pagination.
"""
import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Gets results from CSV file starting from a given index.
        """
        self.dataset()
        self.indexed_dataset()

        assert index < len(self.__dataset)

        data = []
        maximum = max(self.__indexed_dataset.keys())
        next_index = None
        found = 0
        i = 0

        while found < page_size and index + i < maximum:
            if index + i in self.__indexed_dataset.keys():
                item = self.__indexed_dataset.get(index + i)
                data.append(item)
                found += 1
            i += 1

        while index + i < maximum:
            if index + i in self.__indexed_dataset.keys():
                next_index = index + i
                break
            i += 1

        results = {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }

        return results
