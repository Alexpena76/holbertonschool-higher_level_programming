#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_empty_list(self):
        """Test empty list returns None"""
        self.assertIsNone(max_integer([]))
    
    def test_no_argument(self):
        """Test function with no arguments (uses default empty list)"""
        self.assertIsNone(max_integer())
    
    def test_single_element(self):
        """Test list with single element"""
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([0]), 0)
    
    def test_positive_numbers(self):
        """Test list with positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([10, 5, 8, 3]), 10)
    
    def test_negative_numbers(self):
        """Test list with negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -8, -3]), -3)
        self.assertEqual(max_integer([-100, -1]), -1)
    
    def test_mixed_numbers(self):
        """Test list with mixed positive and negative integers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([10, -5, 8, -3]), 10)
        self.assertEqual(max_integer([-10, -5, 0, -3]), 0)
    
    def test_duplicate_max(self):
        """Test list where maximum value appears multiple times"""
        self.assertEqual(max_integer([1, 2, 3, 3, 2]), 3)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([-1, -1, -2]), -1)
    
    def test_max_at_beginning(self):
        """Test where maximum is the first element"""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)
        self.assertEqual(max_integer([0, -1, -2, -3]), 0)
    
    def test_max_at_end(self):
        """Test where maximum is the last element"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)
        self.assertEqual(max_integer([-3, -2, -1, 0]), 0)
    
    def test_max_in_middle(self):
        """Test where maximum is in the middle"""
        self.assertEqual(max_integer([1, 10, 2, 3]), 10)
        self.assertEqual(max_integer([-5, 0, -3, -1]), 0)
    
    def test_large_numbers(self):
        """Test with large integers"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)
        self.assertEqual(max_integer([-1000000, -999999, -1000001]), -999999)
    
    def test_long_list(self):
        """Test with longer list"""
        long_list = list(range(100))  # [0, 1, 2, ..., 99]
        self.assertEqual(max_integer(long_list), 99)
        
        long_list_desc = list(range(99, -1, -1))  # [99, 98, ..., 0]
        self.assertEqual(max_integer(long_list_desc), 99)
    
    def test_two_elements(self):
        """Test with exactly two elements"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)
        self.assertEqual(max_integer([-1, -2]), -1)
    
    def test_zero_included(self):
        """Test lists that include zero"""
        self.assertEqual(max_integer([0, 1, 2]), 2)
        self.assertEqual(max_integer([-1, 0, -2]), 0)
        self.assertEqual(max_integer([0, 0, 0]), 0)


if __name__ == '__main__':
    unittest.main()
