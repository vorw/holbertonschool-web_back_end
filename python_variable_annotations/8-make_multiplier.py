#!/usr/bin/env python3
"""Takes float multiplier, returns a function that multiplies floats."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns function that multiplies by multiplier."""

    def multiply(n: float) -> float:
        """Multiplies n by multiplier."""
        return n * multiplier

    return multiply