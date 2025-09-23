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

    def test_multiple_instances(self):
        """Test creating multiple Square instances"""
        square1 = Square()
        square2 = Square()

        self.assertIsNot(square1, square2)

        self.assertEqual(type(square1), type(square2))

    def test_square_is_class(self):
        """Test that Square is actually a class"""
        self.assertTrue(isinstance(Square, type))

    def test_square_module(self):
        """Test that Square class belongs to the correct module"""
        self.assertEqual(Square.__module__, '0-square')

if __name__ == '__main__':
    unittest.main()