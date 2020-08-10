
class _DoublyLinkedBase:
    class _Node:
        __slots__ = '_element','_next','_prev'
        def __init__(self,element,_next,prev):
            self._element = element
            self._prev = prev
            self._next = _next
    def __init__(self):
        #sentinals
        self._header = self._Node(None,None,None)
        self._footer = self._Node(None,None,None)

        #link the header and footer
        self._header._next = self._footer
        self._footer._prev = self._header

        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self,value,predecessor,successor):
        new_node = self._Node(value,successor,predecessor)
        successor._prev = new_node
        predecessor._next = new_node
        self._size += 1
        return new_node

    def _remove_element(self,Node):
        predecessor = Node._prev
        successor = Node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        temp = Node 
        Node._element = Node._next = Node._prev = None
        return temp._element
class Deque(_DoublyLinkedBase):
    def first(self):
        if 
        return self._header._next._element

     def last(self):
         return self._tail._next._element   