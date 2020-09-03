"""

"""
import pytest
from maplayerpy.maplayer import BasicLayer, BasicLayerRow


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
        _ = BasicLayerRow((1, 2, 3))


def test_basic_row_eq_returns_true_on_equal_rows():
    r1 = BasicLayerRow[int]([1, 2, 3])
    r2 = BasicLayerRow[int]([1, 2, 3])
    assert r1 == r2


def test_basic_row_eq_returns_false_on_rows_different_length():
    r1 = BasicLayerRow[int]([1, 2, 3, 4])
    r2 = BasicLayerRow[int]([1, 2])
    assert (r1 == r2) is False


def test_basic_row_eq_returns_false_on_rows_same_length_different_contents():
    r1 = BasicLayerRow[int]([1, 2, 3])
    r2 = BasicLayerRow[int]([2, 3, 2])
    assert (r1 == r2) is False


def test_basic_layer_eq_returns_true_on_equal_layers():
    r1 = BasicLayer[int]([[1, 2, 3], [4, 5, 6]])
    r2 = BasicLayer[int]([[1, 2, 3], [4, 5, 6]])
    assert r1 == r2


def test_basic_layer_eq_returns_false_on_rows_different_length():
    r1 = BasicLayer[int]([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    r2 = BasicLayer[int]([[1, 2, 3], [4, 5, 6]])
    assert (r1 == r2) is False


def test_basic_layer_eq_returns_false_on_rows_same_length_different_contents():
    r1 = BasicLayer[int]([[1, 2, 3], [6, 5, 4]])
    r2 = BasicLayer[int]([[1, 2, 3], [4, 5, 6]])
    assert (r1 == r2) is False
