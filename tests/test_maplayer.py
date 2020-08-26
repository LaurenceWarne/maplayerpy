"""

"""
import unittest

from maplayerpy.maplayer import BasicLayer


class TestBasicLayer(unittest.TestCase):

    def test_instantiating_with_jagged_arrays_raises_value_error(self):
        with self.assertRaises(ValueError):
            _ = BasicLayer([[1], [1, 2]])

    def test_instantiating_with_non_nested_sequence_raises_type_error(self):
        with self.assertRaises(TypeError):
            _ = BasicLayer([1, 2])

    def test_instantiating_with_inner_container_immutable_raises_type_error(self):
        with self.assertRaises(TypeError):
            _ = BasicLayer([(1, 3), [1, 2]])
