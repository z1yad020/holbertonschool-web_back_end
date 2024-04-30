#!/usr/bin/env python3

"""
basic annot - ducck duck
"""

from typing import List, Union, Tuple, Callable, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Let's duck type an iterable object"""
    return [(i, len(i)) for i in lst]
