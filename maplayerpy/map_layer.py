"""
This file contains abstract base classes for MapLayer objects along
with some useful mixins.
"""
from abc import abstractmethod
from typing import MutableSequence, TypeVar

T = TypeVar("T")


class MapLayer(MutableSequence[T]):
    """A wrapper around MutableSequence."""

    @abstractmethod
    def width(self) -> int:
        pass


class BasicLayer(MapLayer[T]):
    """
    A basic MapLayer implementation which delegates method calls to
    a nested sequence.
    """

    def __init__(self, table: MutableSequence[MutableSequence[T]]):
        self._table = table

    def width(self) -> int:
        return len(self._table[0]) if len(self._table) > 1 else 0

    def __len__(self) -> int:
        return len(self._table)

    def __getitem__(self, key: int) -> MutableSequence[T]:
        return self._table[key]

    def __str__(self) -> str:
        return str(self._table)

    def __repr__(self) -> str:
        return "BasicLayer(" + repr(self._table) + ")"
