class Queue:
    class _Node:
        def __init__(self,value,_next):
            self._value = value
            self._next = _next
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0 
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def dequeue(self):
        if self.is_empty():
            raise LookupError('Queue has zero elements')
        temp = self._head._value
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return temp

    def enqueue(self,value):
        newest = self._Node(value, self._head)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def __str__(self):
        temp = [None] * self._size
        current = self._head
        for i in range(self._size):
            temp[i] = current._value
            current = current._next
        return str(temp) 
if __name__ == '__main__':
    ting = Queue()
    [ting.enqueue(i) for i in range(2,20)]
    print(ting)