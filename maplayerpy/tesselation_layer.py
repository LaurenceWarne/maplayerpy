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
        """Return 'centres' for each region."""
        pass

    @abstractmethod
    def random_cell_in_region(self, region: int) -> Tuple[int, int]:
        """Return the coordinates of a random cell in region."""
        pass

    @property
    def no_regions(self) -> int:
        """Return the number of regions in this tesselation."""
        return len(self.points)
