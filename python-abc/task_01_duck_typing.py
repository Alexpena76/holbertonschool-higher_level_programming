#!/usr/bin/python3
"""Module that provides Shape abstract class and its implementations"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract Shape class"""

    @abstractmethod
    def area(self):
        """Abstract method to calculate area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter"""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape"""

    def __init__(self, radius):
        """
        Initialize a Circle with radius

        Args:
            radius: radius of the circle
        """
        self.radius = radius

    def area(self):
        """
        Calculate and return the area of the circle

        Returns:
            Area of the circle (π * r²)
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate and return the perimeter of the circle

        Returns:
            Perimeter of the circle (2 * π * r)
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape"""

    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate and return the area of the rectangle

        Returns:
            Area of the rectangle (width * height)
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle

        Returns:
            Perimeter of the rectangle (2 * (width + height))
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape using duck typing

    Args:
        shape: any object that has area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
