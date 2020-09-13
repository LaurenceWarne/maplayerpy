import random

import numpy as np
import pytest
from maplayerpy.voronoi_layer import (VoronoiLayer, get_random_points_spaced,
                                      get_random_voronoi_layer,
                                      get_voronoi_layer)


@pytest.mark.voronoi_img
def test_voronoi_img():
    import cv2
    no_points = 20
    random.seed(1034321)
    layer = get_random_voronoi_layer(500, 500, no_points)
    arr = (256 // no_points) * np.array(layer, dtype=np.int16)
    cv2.imwrite("examples/voronoi.png", arr)


def test_get_voronoi_layer_returns_correct_map():
    layer = get_voronoi_layer(
        4, 4, [(0, 0), (1, 1)],
        lambda x, y, px, py: 0 if (
            ((x + y) < 2 and px == 0) or ((x + y) >= 2 and px == 1)
        ) else 1
    )
    assert [
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
    ] == [
        [layer[0][0], layer[0][1], layer[0][2], layer[0][3]],
        [layer[1][0], layer[1][1], layer[1][2], layer[1][3]],
        [layer[2][0], layer[2][1], layer[2][2], layer[2][3]],
        [layer[3][0], layer[3][1], layer[3][2], layer[3][3]],
    ]


def test_voronoi_obj_points_are_correct():
    layer = get_voronoi_layer(
        4, 4, [(0, 0), (1, 1)]
    )
    assert [(0, 0), (1, 1)] == layer.points


def test_voronoi_no_regions_is_correct():
    layer = get_voronoi_layer(
        4, 4, [(0, 0), (1, 1)]
    )
    assert 2 == layer.no_regions


def test_cannot_set_points_in_voronoi_obj():
    layer = get_voronoi_layer(
        4, 4, [(0, 0), (1, 1)]
    )
    with pytest.raises(AttributeError):
        layer.points = [(3, 4)]


def test_cannot_set_no_regions_in_voronoi_obj():
    layer = get_voronoi_layer(
        4, 4, [(0, 0), (1, 1)]
    )
    with pytest.raises(AttributeError):
        layer.no_regions = 342


def test_get_random_points_spaced_returns_correct_no_points():
    spacing = 5
    random.seed(10132123)
    pts, is_valid = get_random_points_spaced(
        100, 100, spacing, 10
    )
    assert 10 == len(pts)


def test_get_random_points_spaced_returns_spaced_points_on_valid():
    spacing = 5
    random.seed(10132123)
    pts, is_valid = get_random_points_spaced(
        100, 100, spacing, 10
    )
    assert is_valid is True
    for idx, (px1, py1) in enumerate(pts):
        for (px2, py2) in pts[:idx]:
            d = np.sqrt((px1 - px2) * (px1 - px2) + (py1 - py2) * (py1 - py2))
            assert d > spacing


def test_get_random_points_spaced_returns_false_on_impossible_no_points():
    spacing = 5
    random.seed(18934053)
    pts, is_valid = get_random_points_spaced(
        10, 10, spacing, 20
    )
    assert is_valid is False


def test_get_voronoi_layer_random_cell_returns_point_in_region():
    random.seed(580324750)
    layer = VoronoiLayer(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ], [(0, 0), (5, 5)], 3
    )
    x, y = layer.random_cell_in_region(1)
    assert 1 == layer[y][x]
