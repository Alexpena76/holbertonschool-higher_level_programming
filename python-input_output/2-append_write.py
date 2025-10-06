#!/usr/bin/python3
"""Module that provides a function to append a string to a text file"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns
    the number of characters added

    Args:
        filename: path to the file to append to
        text: string to append to the file

    Returns:
        Number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
