"""

"""
from abc import abstractmethod
from typing import Sequence, Tuple

from .maplayer import MapLayer


class TesselationLayer(MapLayer[int]):

    @property
    @abstractmethod
    def points(self) -> Sequence[Tuple[int, int]]:
        pass

    @abstractmethod
    def random_point_in_region(self, region: int) -> Tuple[float, float]:
        pass

    @abstractmethod
    def random_cell_in_region(self, region: int) -> Tuple[int, int]:
        pass

    @property
    def no_points(self) -> int:
        return len(self.points)
