#!/usr/bin/env python3

"""
Simple helper function
"""


import csv
import math
from typing import List, Dictionary


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page from dataset
        """
        assert type(page) is int and type(page_size) is int\
            and page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """get hyper"""
        data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) // page_size\
            if len(self.dataset()) % page_size == 0\
            else len(self.dataset()) // page_size + 1
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }


def index_range(page: int, page_size: int) -> tuple:
    """index_range"""
    return ((page - 1) * page_size, page * page_size)
