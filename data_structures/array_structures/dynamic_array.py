#an implementation of the Dynamic Array from the book page 196
import ctypes

class DynamicArray:
    def __init__(self):
        self._capacity = 1
        self._n = 0
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._capacity

    def __getitem__(self,k):
        if k < 0:
            k += self._capacity
        if not 0 <= k < self._n:
            raise IndexError('Index out of range')
        return self._A[k]

    def _resize(self,l):
        B = self._make_array(l)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = l


    def append(self,obj):
        if self._capacity == self._n:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _make_array(self,c):
        return (c * ctypes.py_object )()

    def remove(self,val):

        for k in range(self._n):
            if self._A[k] == val:
                for i in range(k,self._n - 1):
                    self._A[i] =self._A[i + 1]
                self._A[self._n - 1] = None
                self._n -= 1    
    
    def insert(self,k,val):
        for i in range(self._n,k,-1):
            self._A[i] = self._A[i + 1]
        self._A[k] = val
        self._n += 1

    def __repr__(self):
        return f'{[self._A[n] for n in range(self._n)]}'

ting = DynamicArray()


print(ting)