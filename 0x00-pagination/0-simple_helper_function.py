#!/usr/bin/env python3
"""Pagination helper function.
"""
from typing import Tuple
def index_range(page: int, page_size: int) -> Tuple[int, int]:
    
    size = (page-1)* page_size
    return(size, size + page_size)
