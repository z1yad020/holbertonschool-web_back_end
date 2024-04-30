#!/usr/bin/env python3

"""
basic annot - func
"""

from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Complex types - functions"""
    return lambda x: x**2
