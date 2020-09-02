"""

"""
import unittest

from maplayerpy.maplayer import BasicLayer, BasicMapLayerRow


class TestBasicLayer(unittest.TestCase):

    def test_can_create_basic_layer_with_mutable_sequence(self):
        _ = BasicLayer([[1, 2], [3, 4]])

    def test_creating_basic_layer_with_jagged_list_raises_value_error(self):
        with self.assertRaises(ValueError):
            _ = BasicLayer([[1], [1, 2]])

    def test_creating_basic_layer_with_non_nested_sequence_raises_type_error(self):
        with self.assertRaises(TypeError):
            _ = BasicLayer([1, 2])

    def test_creating_basic_layer_with_inner_container_immutable_raises_type_error(self):
        with self.assertRaises(TypeError):
            _ = BasicLayer([(1, 3), [1, 2]])

    def test_creating_basic_row_with_immutable_seq_raises_type_error(self):
        with self.assertRaises(TypeError):
            _ = BasicMapLayerRow((1, 2, 3))
