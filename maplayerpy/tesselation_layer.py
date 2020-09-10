"""
Abstract class for using tesselated MapLayers.
"""
from abc import abstractmethod
from typing import Sequence, Tuple

from .maplayer import MapLayer


class TesselationLayer(MapLayer[int]):
    """
    Represents a layer split up into a finite number of regions, with
    each cell belonging to exactly one region.
    """

    @property
    @abstractmethod
    def points(self) -> Sequence[Tuple[int, int]]:
        pass

    @abstractmethod
    def random_cell_in_region(self, region: int) -> Tuple[int, int]:
        pass

    @property
    def no_points(self) -> int:
        return len(self.points)
