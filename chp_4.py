import random
#factorial
def factorial(n):
    if n == 1: return n
    return n * factorial(n-1)
print(factorial(10))

#English ruler

def ruler(n):
    #base case the last value
    if float(n).is_integer(): print(f'----{int(n)}')
    elif n % .5 == 0: print(f'---') 
    elif n % .25 == 0: print(f'--') 
    elif n % .125 == 0: print(f'-')
    if n == 0: return 0
    return ruler(n - (1/8))
    #conditionals 
# ruler(4)

#solution in the book
def interval(center):
    if center > 0:
        interval(center - 1)
        print('-'*(center - 1),end='\n')
        interval(center - 1)
interval(1)

#bad fibonaci
def fibonaci_mk1(n):
    if n <= 1:
        return n
    else:
        return fibonaci_mk1(n-1) + fibonaci_mk1(n-2)

print(fibonaci_mk1(4))

#better fibonaci 
def fibonaci(n):
    if n <= 1:
        return (n,n-1)
    a,b = fibonaci(n-1)
    return (a+b, a)
print(fibonaci(4))

#binary search 
def binary_search(arr,l,h,x):
    mid = (h + l) // 2
    if l < h:
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return binary_search(arr,l,mid - 1,x)
        else:
            return binary_search(arr,mid + 1,h,x)
    return False
_list =[15, 21, 33, 34, 51, 52, 63, 72, 74]
print(_list)
# print(binary_search(_list,0,len(_list),69 ))

def _sum(seq):
    if len(seq) == 1: return seq[len(seq) - 1]
    return seq[0] + _sum(seq[1:])

print(_sum([5,4,3,2,1]))
print(sum([5,4,3,2,1]))

def reverse(seq,start,stop):
    '''
        - make stop len - 1
    '''
    if start < stop:
        seq[start], seq[stop] = seq[stop], seq[start]
        reverse(seq,start + 1, stop - 1)
reverse(_list,0,len(_list) - 1)
print(_list)
