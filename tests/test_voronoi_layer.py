import random

import numpy as np
import pytest
from maplayerpy.voronoi_layer import (get_random_voronoi_layer,
                                      get_voronoi_layer)


def test_get_voronoi_layer_returns_correct_map():
    layer = get_voronoi_layer(
        4, 4, [(0, 0), (1, 1)],
        lambda x, y, px, py: 0 if (
            ((x + y) < 2 and px == 0) or ((x + y) >= 2 and px == 1)
        ) else 1
    )
    assert [
        [layer[0][0], layer[0][1], layer[0][2], layer[0][3]],
        [layer[1][0], layer[1][1], layer[1][2], layer[1][3]],
        [layer[2][0], layer[2][1], layer[2][2], layer[2][3]],
        [layer[3][0], layer[3][1], layer[3][2], layer[3][3]],
    ] == [
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
    ]


@pytest.mark.voronoi_img
def test_voronoi_img():
    import cv2
    no_points = 20
    random.seed(10)
    layer = get_random_voronoi_layer(
        500, 500, no_points,
    )
    arr = (256 // no_points) * np.array(layer, dtype=np.int16)
    cv2.imwrite("voronoi.png", arr)
