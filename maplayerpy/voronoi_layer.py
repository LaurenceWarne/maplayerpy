"""

"""
from typing import Sequence, Tuple

from .map_layer import BasicLayer


class VoronoiLayer(BasicLayer[int]):
    def __init__(
            self, table: Sequence[Sequence[int]],
            points: Sequence[Tuple[int, int]]
    ):
        self._table = table
        self.points = points
        self.no_points = len(self.points)


def get_voronoi_layer(width: int, height: int, no_points: int) -> VoronoiLayer:
    """Creates a Voronoi diagram."""
    pass
