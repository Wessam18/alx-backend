#!/usr/bin/env python3
"""import module"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ """
    start_indx = ((page - 1) * page_size)
    end_indx = (start_indx + page_size) 
    return (start_indx, end_indx)
