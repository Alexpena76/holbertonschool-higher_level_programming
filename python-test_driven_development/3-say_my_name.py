#!/usr/bin/python3
"""
This module provides a function to print a person's name.
It handles validation of string inputs for first and last names.
The function ensures both arguments are strings before formatting output.
Provides clear error messages for invalid input types.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted name string with first and last names.
    Validates that both arguments are strings before printing.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))
