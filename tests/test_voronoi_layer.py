import unittest

from maplayerpy.voronoi_layer import get_voronoi_layer


class TestBasicLayer(unittest.TestCase):

    def test_get_voronoi_layer_returns_correct_map(self):
        layer = get_voronoi_layer(
            4, 4, [(0, 0), (1, 1)],
            lambda x, y, px, py: 0 if (
                ((x + y) < 2 and px == 0) or ((x + y) >= 2 and px == 1)
            ) else 1
        )
