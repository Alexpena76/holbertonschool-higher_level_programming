#!/usr/bin/python3
"""Module that provides Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height

        Args:
            width: width of the rectangle (must be positive integer)
            height: height of the rectangle (must be positive integer)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
