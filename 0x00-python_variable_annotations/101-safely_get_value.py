#!/usr/bin/env python3

"""Python annotations - safely get value"""
from typing import TypeVar, Dict, Optional

T = TypeVar('T')


def safely_get_value(dct: Dict[str, T], key: str, default: Optional[T] = None) -> Optional[T]:
    """
    safely get value from dict
    """
    if key in dct:
        return dct[key]
    else:
        return default
