#!/usr/bin/env python3
"""index_range function"""
from typing import Tuple


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
