#!/usr/bin/env python3
"""This module has a type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A type-annotated function sum_list which takes a list input_list
        of floats as argument and returns their sum as a float.
    """

    return sum(mxd_lst)
