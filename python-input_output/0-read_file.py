#!/usr/bin/python3
"""Module that provides a function to read and print a text file"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout

    Args:
        filename: path to the file to read
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
