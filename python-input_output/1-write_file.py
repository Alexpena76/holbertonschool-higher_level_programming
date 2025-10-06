#!/usr/bin/python3
"""Module that provides a function to write a string to a text file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns number of characters written

    Args:
        filename: path to the file to write
        text: string to write to the file

    Returns:
        Number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
