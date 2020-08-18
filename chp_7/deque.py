from doubly_linked_list import _DoublyLinkedBase
import random

class Deque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise ValueError('The deque has zero elements')
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise ValueError('The deque has zero elements')
        return self._footer._prev._element
    
    def add_first(self,value):
        self._insert_between(value,self._header,self._header._next)
    
    def add_last(self,value):
        self._insert_between(value,self._footer._prev,self._footer)


    def remove_first(self):
        if self.is_empty():
            raise ValueError('There are no more elements left')
        self._remove_element(self._header._next)

    def remove_last(self):
        if self.is_empty():
            raise ValueError('There are no more elements left')
        self._remove_element(self._footer._prev)
    
    def __str__(self):
        current = self._header._next
        list_  = [] 
        for i in range(self._size):
            if i == 0: list_ += 'Head '
            list_ += f'[{current._element}] -> '
            if i == self._size  - 1: list_ += ' Tail'
            current = current._next
        return ''.join(list_)
if __name__ == '__main__':
    ting = Deque()
    [ting.add_first(n) for n in random.sample(range(100),10)]
    print(ting)
    print(ting.first())