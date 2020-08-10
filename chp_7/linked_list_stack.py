#implementation of singly linked list 

class Stack:
    class _Node:
        __slots__ ='_element','_next'
        def __init__(self,element,_next):
            self._element= element
            self._next = _next

    def __init__(self,head = None):
        self._head = self._Node(head,None)
        self._size = 0
    def pop(self):
        if self.is_empty():
            raise LookupError('List is empty')

        temp = self._head._element
        self._head = self._head._next
        self._size -= 1 
        return temp

    def push(self,value):
        self._head = self._Node(value,self._head)
        self._size += 1
    
    def __len__(self):
        return self._size
        
    def top(self):
        if self.is_empty():
            raise LookupError('List is empty')
        return self._head._element

    def is_empty(self):
        return self._size == 0
    
    def __str__(self):
        temp = [None] * self._size
        current = self._head
        for i in range(self._size):
            temp[i] = current._element
            current = current._next
        return str(temp)
if __name__ == '__main__':
    ting = Stack()
    [ting.push(i) for i in range(10)]
    print(ting)
    print(ting.pop())
    print(ting)
    print(ting.top())
    print(len(ting))
    print(ting)