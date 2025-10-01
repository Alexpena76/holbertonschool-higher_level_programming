#!/usr/bin/python3
"""Module that provides BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with area and integer_validator methods"""

    def area(self):
        """Raises an Exception with message: area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0

        Args:
            name: string name of the value
            value: value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
