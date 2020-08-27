
class PriorityQueue:
    class _Item:
        '''
            - light weight object that contains a key and a value 
        '''

        __slots__ = '_key','_value'

        def __init__(self,k,v):
            self._key = k 
            self._value = v

        def __it__(self,other):
            return self._key < other._key
        
        def is_empty(self):
            '''
                - Return True if the priority queue is empty 
            '''
            return len(self) == 0

        def __gt__(self,other):
            if not isinstance(other,type(self)):
                raise ValueError('The adjacent value cannot be compared to this value')
            return self._value > other._value