#!/usr/bin/python3
"""
This module provides a function to print a square using # characters.
It handles validation of size parameter and ensures proper formatting.
The function validates that size is a non-negative integer before printing.
Provides clear error messages for invalid input types and values.
"""


def print_square(size):
    """
    Prints a square made of # characters with the given size.
    Size must be a non-negative integer.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
