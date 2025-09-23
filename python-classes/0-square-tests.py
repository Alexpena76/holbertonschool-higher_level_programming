#!/usr/bin/python3
"""Test file for Square class"""
import unittest
Square = __import__('0-square').Square


class TestSquare(unittest.TestCase):
    """Test cases for the empty Square class"""

    def test_square_creation(self):
        """Test that Square instances can be created"""
        square = Square()
        self.assertIsInstance(square, Square)

if __name__ == '__main__':
    unittest.main()