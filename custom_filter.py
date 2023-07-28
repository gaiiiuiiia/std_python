from __future__ import annotations
from collections.abc import Callable, Sequence

__all__ = [
    'custom_filter',
    'FilterObject',
]


def custom_filter(func: Callable, collection: Sequence) -> FilterObject:
    if isinstance(collection, FilterObject):
        return collection.add_filter(func)
    return FilterObject(func, collection)


class FilterObject:
    def __init__(self, func: Callable, sequence: Sequence) -> None:
        self._sequence = sequence
        self._filter_funcs = [func]
        self.__index = 0

    def add_filter(self, func) -> FilterObject:
        self._filter_funcs.append(func)
        return self

    def _check_filters(self, item) -> bool:
        for func in self._filter_funcs:
            if not func(item):
                return False
        return True

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self._sequence[self.__index]
        except IndexError:
            raise StopIteration

        self.__index += 1

        if not self._check_filters(item):
            return next(self)

        return item
