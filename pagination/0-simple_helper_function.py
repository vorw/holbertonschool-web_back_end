#!/usr/bin/env python3
"""
returns a tuple of size two containing a start index and an end index
for pagination
"""


def index_range(page, page_size):
    """function for tuple making"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
