import unittest
from data_types_lab.data_type import data_type


class DataTypeComparisons(unittest.TestCase):
    def test_string_type_arg(self):
        """
        For argument of string type, data_type should return the length of the string
        """
        self.assertEqual(3, data_type('abc'))

    def test_none_type_arg(self):
        """
        For None args, data_type should return a string 'no_value'
        """
        self.assertEqual('no value', data_type(None))

    def test_boolean_type_args(self):
        """
        For boolean args, data_type should simply return the boolean arg
        """
        self.assertEqual(True, data_type(True))

    def test_integer_type_args_equal_100(self):
        """
        For integer type args, data_type should compare the arg to 100.
        """
        self.assertEqual('equal to 100', data_type(100))

    def test_integer_type_args_less_than_100(self):
        """
        For integer type args, data_type should compare the arg to 100.
        """
        self.assertEqual('less than 100', data_type(2))

    def test_integer_type_args_more_than_100(self):
        """
        For integer type args, data_type should compare the arg to 100.
        """
        self.assertEqual('more than 100', data_type(101))

    def test_list_type_args_with_third_arg(self):
        """
        For list type args, data_type should return the 3rd item in the list otherwise None
        """
        self.assertEqual('c', data_type(['a', 'b', 'c']))

    def test_list_type_args_without_third_arg(self):
        """
        For list type args, data_type should return the 3rd item in the list otherwise None
        """
        self.assertEqual(None, data_type([]))
