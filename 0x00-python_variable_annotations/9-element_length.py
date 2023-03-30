#!/usr/bin/env python3
"""Python annotations"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Return corresponding types
    """
    return [(i, len(i)) for i in lst]
