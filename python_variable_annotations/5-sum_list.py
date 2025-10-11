#!/usr/bin/env python3
"""Takes list of floats, returns their sum as float."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns sum of list of floats."""
    return float(sum(input_list))