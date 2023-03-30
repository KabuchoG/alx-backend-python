#!/usr/bin/env python3

"""Python annotations"""
from typing import Any

def safe_first_element(lst: list[Any]) -> Any | None:
    """
    Returns the first element of a list if it exists, otherwise returns None.

    Args:
    lst: A list of any type.

    Returns:
    The first element of the input list, or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
