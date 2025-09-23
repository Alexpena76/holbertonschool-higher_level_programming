#!/usr/bin/python3
"""Test file for Square class with size validation"""
import unittest
Square = __import__('2-square').Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class with size validation"""

    def test_square_creation_with_valid_size(self):
        """Test creating Square with valid integer size"""
        square = Square(3)
        self.assertIsInstance(square, Square)
        self.assertEqual(square._Square__size, 3)

    def test_square_creation_default_size(self):
        """Test creating Square with default size (0)"""
        square = Square()
        self.assertIsInstance(square, Square)
        self.assertEqual(square._Square__size, 0)

    def test_square_creation_zero_size(self):
        """Test creating Square with size 0 explicitly"""
        square = Square(0)
        self.assertEqual(square._Square__size, 0)

    def test_square_creation_large_size(self):
        """Test creating Square with large valid size"""
        square = Square(100)
        self.assertEqual(square._Square__size, 100)

    def test_private_size_in_dict(self):
        """Test that private size appears correctly in __dict__"""
        square = Square(5)
        self.assertEqual(square.__dict__, {'_Square__size': 5})

    def test_size_not_accessible_directly(self):
        """Test that size attribute is not accessible directly"""
        square = Square(7)
        with self.assertRaises(AttributeError):
            _ = square.size

    def test_private_size_not_accessible_directly(self):
        """Test that __size is not accessible directly"""
        square = Square(8)
        with self.assertRaises(AttributeError):
            _ = square.__size

    def test_string_size_raises_type_error(self):
        """Test that string size raises TypeError"""
        with self.assertRaises(TypeError) as context:
            Square("3")
        self.assertEqual(str(context.exception), "size must be an integer")

    def test_float_size_raises_type_error(self):
        """Test that float size raises TypeError"""
        with self.assertRaises(TypeError) as context:
            Square(3.14)
        self.assertEqual(str(context.exception), "size must be an integer")

    def test_none_size_raises_type_error(self):
        """Test that None size raises TypeError"""
        with self.assertRaises(TypeError) as context:
            Square(None)
        self.assertEqual(str(context.exception), "size must be an integer")

    def test_list_size_raises_type_error(self):
        """Test that list size raises TypeError"""
        with self.assertRaises(TypeError) as context:
            Square([1, 2, 3])
        self.assertEqual(str(context.exception), "size must be an integer")

    def test_boolean_size_accepted(self):
        """Test that boolean size is accepted (bool is subclass of int in Python)"""
        square_true = Square(True)  # True == 1
        square_false = Square(False)  # False == 0
        self.assertEqual(square_true._Square__size, True)
        self.assertEqual(square_false._Square__size, False)

    def test_negative_size_raises_value_error(self):
        """Test that negative size raises ValueError"""
        with self.assertRaises(ValueError) as context:
            Square(-1)
        self.assertEqual(str(context.exception), "size must be >= 0")

    def test_negative_large_size_raises_value_error(self):
        """Test that large negative size raises ValueError"""
        with self.assertRaises(ValueError) as context:
            Square(-89)
        self.assertEqual(str(context.exception), "size must be >= 0")

    def test_multiple_instances_independent(self):
        """Test that multiple instances have independent sizes"""
        square1 = Square(2)
        square2 = Square(8)
        
        self.assertEqual(square1._Square__size, 2)
        self.assertEqual(square2._Square__size, 8)
        self.assertIsNot(square1, square2)

    def test_type_error_before_value_error(self):
        """Test that TypeError is raised before ValueError for non-integer negative"""
        with self.assertRaises(TypeError) as context:
            Square(-3.5)  # Should raise TypeError, not ValueError
        self.assertEqual(str(context.exception), "size must be an integer")

    def test_error_message_exact_match(self):
        """Test that error messages match exactly"""
        # TypeError message
        try:
            Square("invalid")
        except TypeError as e:
            self.assertEqual(str(e), "size must be an integer")
        
        # ValueError message
        try:
            Square(-10)
        except ValueError as e:
            self.assertEqual(str(e), "size must be >= 0")

    def test_edge_case_large_integer(self):
        """Test with very large valid integer"""
        large_size = 999999
        square = Square(large_size)
        self.assertEqual(square._Square__size, large_size)


if __name__ == '__main__':
    unittest.main()
