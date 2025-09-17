#!/usr/bin/python3
"""
This module provides a function to add two integers.
It handles type validation and casting of float values.
The function ensures both arguments are numeric types before performing addition.
Main purpose is to demonstrate proper input validation and type casting.
"""


def add_integer(a, b=98):
    """
    Adds two integers together after validating and casting inputs.
    Returns the sum as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    if isinstance(a, float) and (a != a or a == float('inf') or a == float('-inf')):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b or b == float('inf') or b == float('-inf')):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
