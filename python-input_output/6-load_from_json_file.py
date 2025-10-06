#!/usr/bin/python3
"""Module that provides a function to load an object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file

    Args:
        filename: path to the JSON file to read

    Returns:
        Python object loaded from the JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
