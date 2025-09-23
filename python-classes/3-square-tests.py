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

    def test_area_calculation_basic(self):
        """Test basic area calculations"""
        square = Square(3)
        self.assertEqual(square.area(), 9)

    def test_area_calculation_different_sizes(self):
        """Test area calculation for different sizes"""
        test_cases = [
            (0, 0),    # 0 * 0 = 0
            (1, 1),    # 1 * 1 = 1
            (2, 4),    # 2 * 2 = 4
            (5, 25),   # 5 * 5 = 25
            (10, 100), # 10 * 10 = 100
        ]
        
        for size, expected_area in test_cases:
            with self.subTest(size=size):
                square = Square(size)
                self.assertEqual(square.area(), expected_area)

    def test_area_large_square(self):
        """Test area calculation for large square"""
        square = Square(100)
        self.assertEqual(square.area(), 10000)

    def test_area_returns_integer(self):
        """Test that area method returns an integer"""
        square = Square(4)
        area = square.area()
        self.assertIsInstance(area, int)

    def test_area_zero_size(self):
        """Test area calculation for zero size"""
        square = Square(0)
        self.assertEqual(square.area(), 0)

    def test_area_default_size(self):
        """Test area calculation for default size (0)"""
        square = Square()
        self.assertEqual(square.area(), 0)

    def test_multiple_area_calls(self):
        """Test that multiple calls to area() return the same result"""
        square = Square(6)
        first_call = square.area()
        second_call = square.area()
        third_call = square.area()
        
        self.assertEqual(first_call, 36)
        self.assertEqual(second_call, 36)
        self.assertEqual(third_call, 36)
        self.assertEqual(first_call, second_call)
        self.assertEqual(second_call, third_call)

    def test_area_different_instances(self):
        """Test area calculation for different instances"""
        square1 = Square(2)
        square2 = Square(7)
        
        self.assertEqual(square1.area(), 4)
        self.assertEqual(square2.area(), 49)
        
        # Ensure they don't interfere with each other
        self.assertNotEqual(square1.area(), square2.area())

    def test_private_size_still_inaccessible(self):
        """Test that size is still private after adding area method"""
        square = Square(4)
        
        with self.assertRaises(AttributeError):
            _ = square.size
        
        with self.assertRaises(AttributeError):
            _ = square.__size

    def test_area_with_boolean_size(self):
        """Test area calculation with boolean sizes"""
        square_true = Square(True)   # True == 1
        square_false = Square(False) # False == 0
        
        self.assertEqual(square_true.area(), 1)  # 1 * 1 = 1
        self.assertEqual(square_false.area(), 0) # 0 * 0 = 0

    def test_validation_still_works(self):
        """Test that size validation still works with area method"""
        # Test TypeError
        with self.assertRaises(TypeError) as context:
            Square("3")
        self.assertEqual(str(context.exception), "size must be an integer")
        
        # Test ValueError
        with self.assertRaises(ValueError) as context:
            Square(-5)
        self.assertEqual(str(context.exception), "size must be >= 0")

    def test_area_method_signature(self):
        """Test that area method has correct signature (no parameters except self)"""
        square = Square(3)
        
        # Should work with no arguments
        result = square.area()
        self.assertEqual(result, 9)
        
        # Should raise TypeError if arguments are passed
        with self.assertRaises(TypeError):
            square.area(5)

    def test_area_calculation_mathematical_correctness(self):
        """Test mathematical correctness of area calculation"""
        # Test perfect squares
        perfect_squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        for i, expected in enumerate(perfect_squares, 1):
            square = Square(i)
            self.assertEqual(square.area(), expected)

    def test_square_dict_unchanged(self):
        """Test that __dict__ still only contains private size"""
        square = Square(7)
        expected_dict = {'_Square__size': 7}
        self.assertEqual(square.__dict__, expected_dict)

    def test_area_access_via_name_mangling(self):
        """Test that we can still access private size via name mangling"""
        square = Square(8)
        self.assertEqual(square._Square__size, 8)
        self.assertEqual(square.area(), 64)
        
        # The area should be consistent with the private attribute
        self.assertEqual(square.area(), square._Square__size ** 2)

if __name__ == '__main__':
    unittest.main()