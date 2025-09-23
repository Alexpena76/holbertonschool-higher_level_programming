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

    def test_square_type(self):
        """Test the type of Square instance"""
        square = Square()
        self.assertEqual(type(square).__name__, 'Square')

    def test_square_empty_dict(self):
        """Test that Square instance has empty __dict__"""
        square = Square()
        self.assertEqual(square.__dict__, {})

if __name__ == '__main__':
    unittest.main()