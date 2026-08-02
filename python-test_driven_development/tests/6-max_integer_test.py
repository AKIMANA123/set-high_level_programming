#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_positive_numbers(self):
        """Test with positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-5, -1, -3, -2]), -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-5, -1, 0, 2]), 2)

    def test_single_element(self):
        """Test with a single element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_duplicate_numbers(self):
        """Test with duplicate numbers"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([1, 2, 2, 3, 3, 3]), 3)

    def test_max_at_beginning(self):
        """Test with max at the beginning"""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)

    def test_max_at_end(self):
        """Test with max at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_max_in_middle(self):
        """Test with max in the middle"""
        self.assertEqual(max_integer([1, 2, 10, 3, 4]), 10)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000, 2000000, 3000000]), 3000000)

    def test_zero_and_negative(self):
        """Test with zero and negative numbers"""
        self.assertEqual(max_integer([0, -1, -2, -3]), 0)

    def test_all_zeros(self):
        """Test with all zeros"""
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_float_numbers(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([-1.5, -0.5, -2.5]), -0.5)

    def test_mixed_int_float(self):
        """Test with mixed integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 1.5]), 3)

    def test_no_argument(self):
        """Test with no argument (using default empty list)"""
        self.assertIsNone(max_integer())

    def test_list_with_strings(self):
        """Test with list of strings"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_list_with_mixed_types(self):
        """Test with mixed types (should still work with strings)"""
        # This will work as expected since strings are comparable
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
        # But we shouldn't mix types that can't be compared

    def test_none_argument(self):
        """Test with None argument"""
        # This would cause an error, but the function doesn't handle None
        # So we test that it raises the appropriate error
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()
