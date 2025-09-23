#!/usr/bin/python3
"""Test file for Square class with area calculation"""
import unittest
Square = __import__('3-square').Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class with area method"""

    def test_area_method_exists(self):
        """Test that area method exists and is callable"""
        square = Square(3)
        self.assertTrue(hasattr(square, 'area'))
        self.assertTrue(callable(square.area))

if __name__ == '__main__':
    unittest.main()