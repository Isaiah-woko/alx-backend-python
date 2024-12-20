#!/usr/bin/env python3
"""This module has a type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A type-annotated function make_multiplier that takes a float
         multiplier as argument and returns a function that multiplies
        a float by multiplier.
    """

    return lambda mul: mul * multiplier
