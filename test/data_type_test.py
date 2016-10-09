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
