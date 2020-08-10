#this has been brought over from chp 6 in the book 
#an implementation of the stack ADT in python 
class Empty(Exception):
    pass
class ArrayStack:
    def __init__(self):
        self._stack = []

    def __len__(self):
        return len(self._stack)
    
    def push(self,value):
        self._stack.append(value)
    
    def pop(self):
        return self._stack.pop()
    
    def top(self):
        if self.is_empty():
            raise Empty('The stack is empty')
        return self._stack[-1]

    def is_empty(self):
        return True if len(self._stack) == 0 else False

ting = ArrayStack()
print(ting.top())


