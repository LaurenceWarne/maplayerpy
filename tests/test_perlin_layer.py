import random

import numpy as np
import pytest
from maplayerpy.perlin_layer import get_perlin_layer


@pytest.mark.perlin_img
def test_perlin_img():
    import cv2
    random.seed(8978324)
    layer = get_perlin_layer(
        500, 500,
        (10, 10)
    )
    mx = np.sqrt(1/2)
    arr = (256 / (2*mx)) * (np.array(layer) + mx)
    cv2.imwrite("examples/perlin.png", arr)
