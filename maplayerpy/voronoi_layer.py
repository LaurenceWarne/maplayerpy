"""
"""
import random
from typing import Callable, Sequence, Tuple

import numpy as np

from .map_layer import BasicLayer


class VoronoiLayer(BasicLayer[int]):
    def __init__(
        self, table: Sequence[Sequence[int]], points: Sequence[Tuple[int, int]]
    ):
        self._table = table
        self.points = points
        self.no_points = len(self.points)


def get_voronoi_layer(
    width: int,
    height: int,
    points: int,
    distance_fn: Callable[[int, int, int, int], float] = lambda x1, y1, x2, y2: (
        x1 - x2
    )
    * (x1 - x2)
    + (y1 - y2) * (y1 - y2),
) -> VoronoiLayer:
    """Creates a Voronoi diagram."""
    arr = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            arr[i][j] = min(distance_fn(j, i, px, py) for (px, py) in points)
    return VoronoiLayer(arr, points)


def get_random_voronoi_layer(
    width: int,
    height: int,
    no_points: int,
    distance_fn: Callable[[int, int, int, int], float] = lambda x1, y1, x2, y2: (
        x1 - x2
    )
    * (x1 - x2)
    + (y1 - y2) * (y1 - y2),
):
    """
    """
    points = zip(
        (random.randint(0, width - 1) for i in range(no_points)),
        (random.randint(0, height - 1) for i in range(no_points)),
    )
    return get_voronoi_layer(width, height, points, distance_fn)
