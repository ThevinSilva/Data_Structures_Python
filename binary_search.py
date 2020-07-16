import random

def binary_search(_list,value):
    # a function that finds the index of a ceratin value in a list
    left = 0
    mid = len(_list)//2 
    right = len(_list) 
    while  left < right: 
        if value < _list[mid]:
            right = mid - 1
        elif _list[mid]< value: 
            left = mid + 1
        else:
            return mid
        mid = (right + left)//2
    else:
        return -1 
_list = sorted(random.sample(range(10),10))
print(_list)    
print(binary_search(_list,6))
print(_list[binary_search(_list,6)])

locations = {'North America': {'USA': ['Mountain View','Atlanta']}, "Asia":{"India":["Bangalore"], "China":["Shanghai"]}}

print(location)