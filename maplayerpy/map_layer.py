"""

"""
from abc import abstractmethod
from typing import Sequence, MutableSequence, TypeVar

T = TypeVar("T")


class MapLayer(Sequence[T]):
    """A wrapper around Sequence."""
    @abstractmethod
    def width(self) -> int:
        pass


class MutableMapLayer(MutableSequence[T], MapLayer[T]):
    """A wrapper around MutableSequence."""
    pass


class BasicLayer(MapLayer[T]):
    def __init__(self, table: Sequence[Sequence[T]]):
        self._table = table

    def width(self) -> int:
        return len(self._table[0])

    def __len__(self) -> int:
        return len(self._table)

    def __getitem__(self, key: int) -> Sequence[T]:
        return self._table[key]

    def __str__(self) -> str:
        return str(self._table)

    def __repr__(self) -> str:
        return "BasicLayer(" + repr(self._table) + ")"
