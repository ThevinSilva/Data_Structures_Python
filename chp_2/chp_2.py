import math
#r-2.9 to r-2.14
class Vector:
    def __init__(self,*args):
        if len(args) == 1:
            self._coords = [0] * args[0]
        else:
            self._coords = list(args)


    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self,k):
        return self._coords[k]
    
    def __setitem__(self,k,val):
        self._coords[k] = val

    def __add__(self,other):
        if len(self) != len(other):
            raise ValueError('dimmensions must be the same')
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    def __radd__(self,other):
        return self + other

    def __sub__(self,other):
        if len(other) != len(self):
            raise ValueError('dimmensions must be the same')
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] - other[i]
        return result 
    
    def __rsub__(self,other):
        if len(other) != len(self):
            raise ValueError('dimmensions must be the same')
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = other[i] - self[i]
        return result 

    def __eq__(self,other):
        return self._coords == other

    def __ne__(self,other):
        return not self._coords == other

    def __mul__ (self,other):
        #scalar constant
        result = Vector(len(self))
        if isinstance(other,int):
            for i in range(len(self)):
                result[i] = other * self[i]
            return result    
        #dot product 
        if len(other) == len(self):
            for i in range(len(self)):
                result[i] = self[i] * other[i]
            return result
    def __rmul__(self,other):
        return self * other
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = - self[i]
        return result 

    def __repr__(self):
        return f'<{str(self._coords)[1:-1]}>'

v1 = Vector(1,2,3,4,5)
v2 = Vector(5)
# for x,y in enumerate([1,2,3,4,5]): v1[x] = y
for x,y in enumerate([1,2,3,4,5]): v2[x] = y
print( v1 * v2 )

#Projects
class Polygon:
    '''
        - ABC for polygons of all shapes and sizes
    '''
    def __init__(self,*args):
            self._lengths = self._len_check(args)
            self._edges = 1

    def _len_check(self,args):
        # make more robust by raising error multi dim lists/tuple
        if len(args) == 1:
            return  args * self._edges
        elif len(args) == self._edges:
             return args
        else:
            raise ValueError(f'{self.__class__.__name__} must have at least three values')

    def area(self):
        pass

    def perimeter(self):
        return sum(self._lengths)

class triangle(Polygon):
    def __init__(self,*args):
        self._edges = 3
        super().__init__(*args) 

    def area(self):
        a,b,c = self._lengths
        # Heron's formula
        p = self.perimeter() / 2

        return math.sqrt( p * (p-a) * (p-b) *( p-c)  )

class quadrilateral(Polygon):
    def __init__(self,*args):
        self._edges = 4
        super().__init__(*args)
    
    def area(self):
        if len(set(self._lengths)) == 1:
            return self._lengths[0] ** 2
        a,b,c,d = self._lengths
        x = math.sqrt(b**2 + c**2)
        print('irregular shape no defined area')
        return triangle(a,b,x).area() + triangle(x,c,d).area()

        #reuse code by breaking the quad into two trangles

print(quadrilateral(13,14,3,13).area())
