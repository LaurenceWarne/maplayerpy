"""

"""
import unittest

from maplayerpy.maplayer import BasicLayer


class TestBasicLayer(unittest.TestCase):

    def test_instantiating_with_jagged_arrays_raised_value_error(self):
        with self.assertRaises(ValueError):
            _ = BasicLayer([[1], [1, 2]])
