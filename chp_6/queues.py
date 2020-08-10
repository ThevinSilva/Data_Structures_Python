class Empty(Exception):
    pass
class Queue:
    MAXIMUM_CAPACITY = 10
    def __init__(self):
        self._data = [None] * Queue.MAXIMUM_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('list empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is emppty')
        temp = self._data[self._front]
        self._data[self._front] = None
        self._front = ( self._front  + 1) % len(self._data)
        self._size -= 1

        #shrinking the array
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return temp
    def enqueue(self,val):
        if self._size == self.__class__.MAXIMUM_CAPACITY:
            self._resize(2 * len(self._data))
        self._data[(self._front + self._size) % len(self._data)] = val
        self._size += 1

    def _resize(self,cap):
        self.__class__.MAXIMUM_CAPACITY =  cap
        temp = [None] * cap
        
        walk = self._front
        for i in range(self._size):
            temp[i] = self._data[walk]
            walk = (1 + walk) % len(self._data)
        self._data = temp
    def __str__(self):
        #''.join([(self._data[n]) if n == self._front else self._data[n] for n in range(self._front,self._size + self._front) ])
        return ''.join([ f'[{self._data[n]}]'if n == self._front else f'<{ self._data[n]}>'  for n in range(len(self._data))])
class Deque(Queue):
    
    def __init__(self):
        super().__init__()
    
    def add_first(self,val):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._data[(self._size + self._front - 1) % len(self._data)] = val
        self._size += 1 

    def add_last(self,val):
        return self.enqueue(val)

    def remove_first(self):
        return self.dequeue()


    def remove_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        last = (self._front - 1) % len(self._data)
        temp = self._data[last]
        self._data[last] = None
        self._size -= 1

        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return temp

    def last(self):
        return self._data[(self._front - 1) % len(self._data)]

if __name__ == '__main__':
    ting= Deque()
    for i in range(20):
        ting.add_first(i)
    print(ting)
    print(ting.remove_first())
    print(ting.remove_first())
    print(ting.first())
    print(ting)