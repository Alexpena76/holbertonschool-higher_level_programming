#!/usr/bin/python3
"""Module that provides Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """
        Initialize a Square with size

        Args:
            size: size of the square (must be positive integer)
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns string representation of the square

        Returns:
            String in format: [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
