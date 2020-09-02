"""
This file contains abstract base classes for MapLayer objects along
with some useful mixins.
"""
from abc import abstractmethod
from typing import MutableSequence, Sequence, TypeVar

from typeguard import typechecked

T = TypeVar("T")


class MapLayerRow(MutableSequence[T]):
    """A wrapper around MutableSequence."""
    pass


class MapLayer(Sequence[MapLayerRow[T]]):
    """A MapLayer encapsulates a two dimensional table.

    The number of rows and columns in the table are fixed, though
    the values present in the table "slots" may be changed.
    """

    @abstractmethod
    def width(self) -> int:
        pass


class BasicMapLayerRow(MapLayerRow[T]):

    @typechecked
    def __init__(self, row: MutableSequence[T]):
        self._row = row

    def __len__(self) -> int:
        return len(self._row)

    def __getitem__(self, key: int) -> MapLayerRow[T]:
        return self._row[key]

    def __setitem__(self, index: int, value: T):
        self._row[index] = value

    def __delitem__(self, item: T):
        self._row.__delitem__(item)

    def insert(self, index: int, item: T):
        self._row.insert(index, item)

    def __str__(self) -> str:
        return str(self._row)

    def __repr__(self) -> str:
        return "BasicLayer(" + repr(self._row) + ")"


class BasicLayer(MapLayer[T]):
    """
    A basic MapLayer implementation which delegates method calls to
    a nested sequence.
    """

    @typechecked
    def __init__(self, table: Sequence[MutableSequence[T]]):
        if len(set(len(row) for row in table)) > 1:
            raise ValueError("table rows are not all of the same length")
        self._table = [BasicMapLayerRow(row) for row in table]

    def width(self) -> int:
        return len(self._table[0]) if len(self._table) > 1 else 0

    def __len__(self) -> int:
        return len(self._table)

    def __getitem__(self, key: int) -> MapLayerRow[T]:
        return self._table[key]

    def __str__(self) -> str:
        return str(self._table)

    def __repr__(self) -> str:
        return "BasicLayer(" + repr(self._table) + ")"
