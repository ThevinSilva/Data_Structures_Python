from ..chp_7 import positional_list

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
