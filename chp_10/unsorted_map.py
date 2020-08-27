from .maps_ABC import MapBase

class UnSrotedTableMap(MapBase):
    # add repr for Item as a sort of extra task 
    def __init__(self):
        self._table = []
    def __getitem__(self,val):
        for item in self._table:
            if val == item._key:
                return item._value
    def __setitem__(self,v,k):
        for item in self._table: 
            if k == item._key:
                item._value = v
                return 
        self._table.append(self._Item(k,v))

    def __delitem__(self,k):
        for i , j in enumerate(self._table):
            if k == j._key:
                self._table.pop(i)
                return
            raise KeyError('Key Error:' + repr(k))
    def __len__(self):
        return len(self._table)
    
    def __iter__(self):
        for item in self._table:
            yield item._key
