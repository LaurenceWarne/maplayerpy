"""
Functions and classes for creating Voronoi diagrams.
"""
import math
import random
from typing import Callable, MutableSequence, Sequence, Tuple

import numpy as np
from typeguard import typechecked

from .maplayer import BasicLayer
from .tesselation_layer import TesselationLayer


class VoronoiLayer(BasicLayer[int], TesselationLayer):
    """A MapLayer implementation of a Voronoi diagram.

    For more information on Voronoi diagrams see:
    https://en.wikipedia.org/wiki/Voronoi_diagram
    """

    @typechecked
    def __init__(
            self,
            table: Sequence[MutableSequence[int]],
            points: Sequence[Tuple[int, int]],
            spacing: int = 4
    ):
        """
        Args:
            table: table corresponding to the Voronoi diagram
            points: points used to construct the Voronoi diagram
            spacing: integer corresponding to the minimum distance
                between any two given points
        """
        super().__init__(table)
        self._points = points
        self._no_points = len(points)
        self._spacing = spacing

    def random_cell_in_region(self, region: int) -> Tuple[int, int]:
        circum_circle_diam = 2 * self._spacing
        # Square circumscribed in circle
        # Here the spacing = the square's side length
        spacing = int(1/2 * math.sqrt(circum_circle_diam**2))
        x, y = self._points[region]
        lx, ly = max(0, x - spacing), max(0, y - spacing)
        hx = min(len(self.table - 1), x + spacing)
        hy = min(len(self.table - 1), y + spacing)
        return (random.randint(lx, hx), random.randint(ly, hy))

    @property
    def points(self) -> Sequence[Tuple[int, int]]:
        """Sequence of points used to generate this Voronoi diagram."""
        return self._points

    @property
    def spacing(self) -> int:
        """The minimum distance between any two given points."""
        return self._spacing


def get_voronoi_layer(
    width: int,
    height: int,
    points: Sequence[Tuple[int, int]],
    distance_fn: Callable[[int, int, int, int], float] =
        lambda x, y, px, py: (x - px) * (x - px) + (y - py) * (y - py)
) -> VoronoiLayer:
    """Return a Voronoi diagram of size width*height.

    Args:
        width: width of the diagram.
        height: height of the diagram.
        points: points used create the diagram.
        distance_fn: function used to obtain the distance between two
            (x, y) points, defaults to Euclidean distance.
    """
    arr = np.zeros((height, width), dtype=np.int16)
    for i in range(height):
        for j in range(width):
            arr[i][j] = min(
                range(len(points)),
                key=lambda idx: distance_fn(
                    j, i, points[idx][0], points[idx][1]
                )
            )
    return VoronoiLayer(arr.tolist(), points)


def get_random_voronoi_layer(
    width: int,
    height: int,
    no_points: int,
    distance_fn: Callable[[int, int, int, int], float] =
        lambda x, y, px, py: (x - px) * (x - px) + (y - py) * (y - py)
) -> VoronoiLayer:
    """Return a random Voronoi diagram of size width*height.

    Args:
        width: width of the diagram.
        height: height of the diagram.
        no_points: number of points to use to create the diagram.
        distance_fn: function used to obtain the distance between two
            (x, y) points, defaults to Euclidean distance.
    """
    points = zip(
        (random.randint(0, width - 1) for i in range(no_points)),
        (random.randint(0, height - 1) for i in range(no_points)),
    )
    return get_voronoi_layer(width, height, list(points), distance_fn)


def get_random_points_spaced(
    width: int,
    height: int,
    spacing: int,
    no_points: int,
    max_iters: int = 100,
    distance_fn: Callable[[int, int, int, int], float] =
        lambda x, y, px, py: np.sqrt((x - px) * (x - px) + (y - py) * (y - py))
) -> Tuple[Sequence[Tuple[int, int]], bool]:
    points, is_valid = list(), True
    for i in range(no_points):
        for j in range(max_iters):
            px = random.randint(0, width - 1)
            py = random.randint(0, height - 1)
            if all(distance_fn(px, py, x, y) > spacing for x, y in points):
                points.append((px, py))
                break
        else:
            points.append((px, py))
            is_valid = False
    return points, is_valid
