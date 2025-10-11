#!/usr/bin/env python3
"""Takes string k and int/float v, returns tuple (k, v²)."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns tuple with string and square of value."""
    return (k, v * v)