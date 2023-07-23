#!/usr/bin/env python3
"""index_range function"""
from typing import Tuple, List
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns the start and end indexes corresponding
    to the given page and page_size.
    Page numbers are 1-indexed, i.e., the first page is page 1.

    :param page: The page number for which to calculate
     the start and end indexes.
    :type page: int
    :param page_size: The number of elements per page.
    :type page_size: int
    :return: A tuple containing the start and end
     indexes for the requested page.
    :rtype: Tuple[int, int]
    :raises ValueError: If page or page_size is not a positive integer.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError(
            "Both 'page' and 'page_size' must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index


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
        """ Finds the correct indexes to paginate dataset.
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        csv_size = len(self.dataset())
        start, end = index_range(page, page_size)
        end = min(end, csv_size)
        if start >= csv_size:
            return []
        return self.dataset()[start:end]
