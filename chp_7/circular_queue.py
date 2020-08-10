
class CicurlarQueue:
    class _Node:
        def __init__(self,value,_next):
            self._value = value
            self._next = _next
    def __init__(self):
        self._tail = None
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    
    def dequeue(self):
        if self.is_empty():
            raise LookupError('The Circular Queue has zero items left')
        old_head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = old_head._next
        self._size -= 1
        return old_head._element
    def enqueue(self,value):
        newest = self._Node(value,None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
            self._tail = newest
            self._size += 1 