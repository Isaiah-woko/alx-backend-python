#!/usr/bin/env python3
"""This module has a type-annotated function make_multiplier"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence if it exists, otherwise returns None."""
    if lst:
        return lst[0]
    else:
        return None
