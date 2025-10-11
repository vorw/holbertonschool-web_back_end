#!/usr/bin/env python3
"""Takes list of int and float, returns total as float."""

from typing import List, Union


def sum_mixed_list(mixed_lst: List[Union[int, float]]) -> float:
    """Returns sum of mixed int/float list."""
    return float(sum(mixed_lst))
    