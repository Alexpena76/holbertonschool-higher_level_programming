#!/usr/bin/python3
"""This module defines a Square class with area calculation"""

class Square:
    """A class that defines a square with size validation and area calculation"""
    def __init__(self, size=0):
        """Initialize a Square with size validation

        Args:
            size (int): The size of the square (default: 0)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

    def area(self):
        """Calculate and return the area of the square
        
        Returns:
            int: The area of the square (size * size)
        """
        return self.__size ** 2
