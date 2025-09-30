#!/usr/bin/python3
"""Module that provides is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or inherited from it

    Args:
        obj: object to check
        a_class: class to compare against

    Returns:
        True if obj is an instance of a_class or a subclass, False otherwise
    """
    return isinstance(obj, a_class)
