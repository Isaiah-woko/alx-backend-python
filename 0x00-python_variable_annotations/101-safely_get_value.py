#!/usr/bin/env python3
"""This module has a type-annotated function"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """Returns the value from the dictionary for a given key
         or a default value."""
    if key in dct:
        return dct[key]
    else:
        return default
