#!/usr/bin/python3
"""
Basic serialization module for Python dictionaries to/from JSON files
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file

    Args:
        data: Python dictionary to serialize
        filename: Name of the output JSON file (will be replaced if exists)
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file

    Args:
        filename: Name of the input JSON file

    Returns:
        Python dictionary with deserialized data from the file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
