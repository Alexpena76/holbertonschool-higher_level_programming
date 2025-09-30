#!/usr/bin/python3
"""Module that provides a lookup function for object attributes and methods"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return dir(obj)
