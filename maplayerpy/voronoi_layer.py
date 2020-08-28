"""
Functions and classes for creating Voronoi diagrams.
"""
import random
from typing import Callable, MutableSequence, Sequence, Tuple

import numpy as np
from typeguard import typechecked

from .map_layer import BasicLayer


class VoronoiLayer(BasicLayer[int]):
    """A MapLayer implementation of a Voronoi diagram.

    For more information on Voronoi diagrams see:
    https://en.wikipedia.org/wiki/Voronoi_diagram
    """

    @typechecked
    def __init__(
            self,
            table: Sequence[MutableSequence[int]],
            points: Sequence[Tuple[int, int]]
    ):
        """
        Args:
            table: table corresponding to the Voronoi diagram
            points: points used to construct the Voronoi diagram
        """
        super().__init__(table)
        self._points = points
        self._no_points = len(points)

    @property
    def points(self) -> Sequence[Tuple[int, int]]:
        """Sequence of points used to generate this Voronoi diagram."""
        return self._points

    @property
    def no_points(self) -> int:
        """Number of points used to generate this Voronoi diagram."""
        return self._no_points


def get_voronoi_layer(
    width: int,
    height: int,
    points: Sequence[Tuple[int, int]],
    distance_fn: Callable[[int, int, int, int], float] = lambda x1, y1, x2, y2: (
        x1 - x2
    )
    * (x1 - x2)
    + (y1 - y2) * (y1 - y2),
) -> VoronoiLayer:
    """Return a Voronoi diagram of size width*height.

    Args:
        width: width of the diagram.
        height: height of the diagram.
        points: points used create the diagram.
        distance_fn: function used to obtain the distance between two
            (x, y) points, defaults to Euclidean distance.
    """
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
    + (y1 - y2) * (y1 - y2)
) -> VoronoiLayer:
    """Return a random Voronoi diagram of size width*height.

    Args:
        width: width of the diagram.
        height: height of the diagram.
        no_points: number of points to use to create the diagram.
        distance_fn: function used to obtain the distance between two
            (x, y) points, defaults to Euclidean distance.
    """    points = zip(
        (random.randint(0, width - 1) for i in range(no_points)),
        (random.randint(0, height - 1) for i in range(no_points)),
    )
    return get_voronoi_layer(width, height, list(points), distance_fn)
