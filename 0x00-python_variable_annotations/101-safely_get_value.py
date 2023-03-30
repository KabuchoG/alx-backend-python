#!/usr/bin/env python3
"""Python annotations"""

from typing import TypeVar, Dict, Any


K = TypeVar('K')  # Type variable for key
V = TypeVar('V')  # Type variable for value


def safely_get_value(dct: Dict[K, V], key: K, default: Any = None) -> V:
    """Returns the value of the key in the dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
