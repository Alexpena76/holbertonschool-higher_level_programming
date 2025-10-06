#!/usr/bin/python3
"""Module that provides a function to convert an object to JSON string"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Args:
        my_obj: object to convert to JSON string

    Returns:
        JSON string representation of the object
    """
    return json.dumps(my_obj)
