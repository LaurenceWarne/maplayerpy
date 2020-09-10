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
    l1 = BasicLayer[int]([[1, 2, 3], [4, 5, 6]])
    l2 = BasicLayer[int]([[1, 2, 3], [4, 5, 6]])
    assert l1 == l2


def test_basic_layer_eq_returns_false_on_rows_different_length():
    l1 = BasicLayer[int]([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    l2 = BasicLayer[int]([[1, 2, 3], [4, 5, 6]])
    assert (l1 == l2) is False


def test_basic_layer_eq_returns_false_on_rows_same_length_different_contents():
    l1 = BasicLayer[int]([[1, 2, 3], [6, 5, 4]])
    l2 = BasicLayer[int]([[1, 2, 3], [4, 5, 6]])
    assert (l1 == l2) is False


def test_can_create_eq_obj_from_basic_layer_row_repr():
    r1 = BasicLayerRow[int]([1, 2, 3])
    assert r1 == eval(repr(r1))


def test_can_create_eq_obj_from_basic_layer_repr():
    l1 = BasicLayer[int]([[1, 2, 3], [6, 5, 4]])
    assert l1 == eval(repr(l1))


def test_basic_layer_row_returns_correct_str():
    r1 = BasicLayerRow[int]([1, 2, 3])
    assert str([1, 2, 3]) == str(r1)


def test_basic_layer_returns_correct_str():
    l1 = BasicLayer[int]([[1, 2, 3], [6, 5, 4]])
    assert """[1, 2, 3]
[6, 5, 4]""" == str(l1)


def test_basic_layer_row_len_returns_correct_length():
    r1 = BasicLayerRow[int]([1, 2, 3])
    assert 3 == len(r1)


def test_basic_layer_len_returns_correct_length():
    l1 = BasicLayer[int]([[1, 2, 3], [6, 5, 4]])
    assert 2 == len(l1)


def test_basic_layer_width_returns_correct_width():
    l1 = BasicLayer[int]([[1, 2, 3], [6, 5, 4]])
    assert 3 == l1.width


def test_basic_layer_width_returns_correct_width_on_no_items():
    l1 = BasicLayer[int]([])
    assert 0 == l1.width
