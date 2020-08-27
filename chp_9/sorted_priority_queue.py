from .priority_queue import PriorityQueue
from ..chp_7.positional_list import PositionalLists

class SortedPriorityQueue(PriorityQueue):
    def __init__(self):
        self._data = PositionalLists()

    def __len__(self):
        return len(self._data)

    def add(self,key,value):
        newest = self._Item(key,value)
        walk = self._data.last()
        while walk is not None and newest < walk.element:
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk,newest)

    def min(self):
        if len(self) <= 0:
            raise ValueError('Queue is empty')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        if len(self) <= 0:
            raise ValueError('Queue is empty')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)

