"""

"""
import pytest
from maplayerpy.maplayer import BasicLayer, BasicMapLayerRow


def test_can_create_basic_layer_with_mutable_sequence():
    _ = BasicLayer([[1, 2], [3, 4]])


def test_creating_basic_layer_with_jagged_list_raises_value_error():
    with pytest.raises(ValueError):
        _ = BasicLayer([[1], [1, 2]])


def test_creating_basic_layer_with_non_nested_sequence_raises_type_error():
    with pytest.raises(TypeError):
        _ = BasicLayer([1, 2])


def test_creating_basic_layer_with_inner_container_immutable_raises_type_error():
    with pytest.raises(TypeError):
        _ = BasicLayer([(1, 3), [1, 2]])


def test_creating_basic_row_with_immutable_seq_raises_type_error():
    with pytest.raises(TypeError):
        _ = BasicMapLayerRow((1, 2, 3))
