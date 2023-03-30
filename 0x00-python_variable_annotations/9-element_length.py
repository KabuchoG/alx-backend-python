#!/usr/bin/env python3
"""Python annotations"""


def element_length(lst: list[str]) -> list[tuple[str, int]]:
    """
    Return corresponding types
    """
    return [(i, len(i)) for i in lst]
