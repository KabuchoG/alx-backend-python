#!/usr/bin/env python3
"""Python annotations"""

from typing import TypeVar

T = TypeVar('T')


def safely_get_value(dct: dict[str, T],
                    key: str, default: T | None = None) -> T | None:
    """
    Returns the value associated with the specified
    key in a dictionary, or a default value if the key is not found.

    Args:
    dct: A dictionary with keys of type str and
    values of type T.
    key: A string representing the key to look up
    in the dictionary.
    default: An optional value of type T that is returned if the key is not
    found in the dictionary.
    Defaults to None.

    Returns:
    The value associated with the specified key in the dictionary,
    or the default value
    if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
