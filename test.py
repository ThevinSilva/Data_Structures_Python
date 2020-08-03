import collections
#DATA STRUCTURES AND ALGORITHMS IN PYTHON by Michael goodrich


_bool = bool(-1)
print(_bool)

#ints / floats 
print(int("A5",16))
print(int(0xA5))
print(float(0xA5))
print(float(6.022e23))
print(int(123213.12312321))

# check for repeats 
print(set(['a', 'b', 'c']))
print({'a', 'b', 'c'})


#lexicographic order ordering 

long = [None] * 100
short = [None] * 12

print(long > short)

long = [1,2,3,4,5]
short = [1,2,3,4,4]

print(long > short)

#sets 
thisset = {"apple", "banana", "cherry"}
subset = {"apple", "banana", "cherry"}

#proper subset 
print( thisset <= thisset)

#precedence
print((5 + 2) /( 3 + 4))

print()

#polymorphic default values 

# def foo(a, b = 15, c):                                                                                                              # this doesn't work
    # pass

def bar(a, b = 15, c=15):
    pass

#map function in python 
_lst_nums = [n for n in range(20)]

_lst_nums = list(map(lambda x : x * x ,_lst_nums))

print(_lst_nums,long,short,sep= " : ",end="\n")

fp = open("./shit.txt","r")

def _index(_lst : list, _val: int) -> int:
    if not isinstance(_lst,collections.Iterable):
        raise TypeError("enter either list or tuple")
    if not isinstance(_val,int):
        raise TypeError("enter a integer value")
    
    return _lst[_val]
    

print(_index(_lst_nums, 2))


# age = -1 # an initially invalid choice
# while age <= 0:
#     try:
#         age = int(input( "Enter your age in years: "))
#         if age <= 0:
#             print( "Your age must be positive")
#     except ValueError:
#         print( "That is an invalid age specification ")
#         raise
    # except EOFError:
    #     print( "There was an unexpected error reading input. ")
    #     # raise

#iterators

i = iter(_lst_nums)
try:
    while False:#change this to check the ting
        print(next(i))
except StopIteration:
    print("you done goofed there bud")
finally:
    pass

_lst_nums = [n for n in range(20)]

#Generators

def factors(n):
    return [k for k in range(1,n + 1) if n % k == 0 ] 

print(factors(100))

def factors_ting(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k

for i in factors_ting(100):
    print(i, end = " ")

#fibonaci generator

def fibonaci():
    a = 0 
    b = 1 
    while True:
        yield a
        a, b = b, a + b

        
ting = fibonaci()
total = 0
x = 0
while x < 4e6:
    x = next(ting)
    total += x if x % 2 == 0 else 0  
print(total)

#list comprehension for square numbers
k = 100
print([n for n in range(1,k + 1) if k % n == 0])

def pal_checker(val):
    mid1, mid2 = (len(val)//2 , len(val)//2 )if len(val) % 2 == 0 else ((len(val) // 2), (len(val) // 2) + 1)
    if (val[0:mid1])[::-1] == val[mid2:len(val)]:
        return True
    return False

# total = 0
# for i in range(int(1e6)):
#     if pal_checker(str(i)) == True and  pal_checker(str(bin(i))[2:]) == True:
#         print(f'{i} & {bin(i)}')  
#         total += i
# print(total)

#scope

#returns things that in current namespace
print(dir())

#r

class Employee(object):
    def __init__(self,first_name,last_name):
        self._first_name = first_name
        self._last_name = last_name
    
    @property
    def email(self):
        return f'{self._first_name}.{self._last_name}@gmail.com'
    
    @email.setter
    def email(self,first_name):
        
    
    @email.setter
    def first_name(self,first_name):
        return self._first_name