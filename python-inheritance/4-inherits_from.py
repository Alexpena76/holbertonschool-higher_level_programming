#!/usr/bin/python3
"""Module that provides inherits_from function"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited from a_class
    
    Args:
        obj: object to check
        a_class: class to compare against
    
    Returns:
        True if obj's class inherited from a_class, False otherwise
        (does not return True if obj is exactly an instance of a_class)
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
