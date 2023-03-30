#!/usr/bin/env pyhon3
"""Python annotations - to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with string k as the first element and the square of
    int/float v as the second element.

    Args:
    k: A string.
    v: An integer or a float.

    Returns:
    A tuple with string k as the first element and the square of int/float
    v as the second element.
    """
    return k, float(v**2)
