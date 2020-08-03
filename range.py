#create a class that overides the python function range()

class Range(object):
    def __init__(self,start,stop=None,step = 1):

        if not stop:
            start, stop = 0 , start

        
        if step == 0:
            raise ValueError("step cannot be 0")

        
        self._length = max(0,(stop - start + step - 1) // step)

        self._start = start
        self._step = step
        self._stop = stop

    def __len__(self):
        return self._length
    def __getitem__(self,k):
        
        if k < 0:
            k += self._length
        if not 0<= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step
    def __contains__(self,val):
        if self._start <= val < self._stop:
            if (val - self._start) % self._step == 0:
                return True
        return False

    def __repr__(self):
        return 'This is the one '

for i in range(23):
    print(i)

print(range(23))


def fibonaic(x):
    # fibonaci
    if x == 1:
        return [0,1]
    return fibonaic(x-1) + [fibonaic(x - 1)[-1] + fibonaic(x-1)[-2] ]


print(fibonaic(4))

def fibonaic2(n,x=0,y=1):
    _lst = [x,y]
    for i in range(1,n - 1):
        _lst[i - 1],_lst[i] = _lst[i - 1],_lst[i] +  _lst[i - 1]

print(fibonaic(10))

print(dir(Range))