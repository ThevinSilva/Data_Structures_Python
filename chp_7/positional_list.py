from .doubly_linked_list import _DoublyLinkedBase
class PositionalLists(_DoublyLinkedBase):
    
#------------------------------- Nested Position List -------------------------------
    class Position:
        def __init__(self,container,node):
            self._container = container
            self._node = node
        
        @property
        def element(self):
            return self._node._element
        
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self,other):
            return not (self == other)
#------------------------------- utility method -------------------------------
    def _validate(self,p):
        print(p._container)
        print(self)
        if not isinstance(p,self.Position):
            raise TypeError('p must be proper position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    def _make_position(self,node):
        if node is self._header or node is self._footer:
            return None
        else:
            return self.Position(self,node)
    def first(self):
        return self._make_position(self._header._next)
    def last(self):
        return self._make_position(self._footer._prev)

    def before(self,p):
        node = self._validate(p)
        return self._make_position(node._prev)
    def after(self,p):
        node = self._validate(p)
        return self._make_position(node._next)
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element
            cursor = self.after(cursor)

#------------------------------- Mutators -------------------------------
    def _insert_between(self,e,predecessor,succesor):
        node = super()._insert_between(e,predecessor,succesor)
        return self._make_position(node)
    
    def add_first(self,e):
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self,e):
        return self._insert_between(e, self._footer._prev, self._footer)
    
    def add_before(self,p,e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    
    def add_after(self,p,e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    
    def delete(self,p):
        original = self._validate(p)
        return self._remove_element(original)

    def replace(self,p,e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

if __name__ == '__main__':
    ting = PositionalLists()
    for i in range(10):
        ting.add_first(i)