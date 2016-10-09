import unittest
from data_types_lab.data_type import data_type


class DataTypeComparisons(unittest.TestCase):
    def test_string_type(self):
        """
        For argument of string type, data_type should return the length of the string
        """
        self.assertEqual(3, data_type('abc'))
