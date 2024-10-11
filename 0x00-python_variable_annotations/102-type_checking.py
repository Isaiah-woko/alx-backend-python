#!/usr/bin/env python3
"""This module has a type-annotated function make_multiplier"""
from typing import Tuple, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """Returns a zoomed-in tuple by repeating each element in the tuple."""
    zoomed_in: Tuple[Any, ...] = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
