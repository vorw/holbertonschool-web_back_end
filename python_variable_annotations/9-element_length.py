#!/usr/bin/env python3
"""Annotates function returning (element, length) pairs."""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns list of (item, length)."""
    return [(i, len(i)) for i in lst]    
