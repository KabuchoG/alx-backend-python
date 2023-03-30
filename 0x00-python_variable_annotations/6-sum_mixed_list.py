#!/usr/bin/env python3
"""Python annotations - sum mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """
    Returns the sum of the mixed list values
    """
    return sum(mxd_lst)
