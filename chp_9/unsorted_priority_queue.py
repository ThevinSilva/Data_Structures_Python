from .priority_queue import PriorityQueue
from ..chp_7.positional_list import PositionalLists

class UnsortedPriorityQueue(PriorityQueue):
    def _find_min(self):
        if len(self) <= 0:
            raise ValueError('List empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element < small.element:
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        self._data = PositionalLists()

    def __len__(self):
        return len(self._data)

    def add(self,key,value):
        self._data.add_last(self._Item(key,value))

    def min(self):
        p = self._find_min()
        item = p.element
        return (item._key , item._value)

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key , item._value)
        