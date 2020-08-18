#couldn't get the positional list to work 
from positional_list import PositionalList

class FavouriteList(PositionalList):
    class _item:
        __slots__ = '_value' , '_count'
        def __init__(self,e):
            self._e =  e
            self._count = 0

#------------------------------- nonpublic utilities -------------------------------

    def _find_position(self,e):
        walk = self._data.first()
        while walk is not None and walk.element._value != e:
            walk = self._data.after(walk)
