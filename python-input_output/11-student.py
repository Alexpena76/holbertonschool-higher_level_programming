#!/usr/bin/python3
"""
Defines a class Student
"""


class Student:
    """Defines a student by first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only those attributes
        listed are retrieved. Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(type(elem) == str for elem in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json: dictionary with attribute names as keys and values as values
        """
        for key, value in json.items():
            setattr(self, key, value)
