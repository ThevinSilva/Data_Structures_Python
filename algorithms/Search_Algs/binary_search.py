"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""
                               
import random
from RunTime import RunTime


@RunTime
def binary_search(input_array, value):
    left = 0
    mid = len(input_array)//2
    right = len(input_array) - 1
    while right >= left:
        if input_array[mid] == value:
            return mid
        if input_array[mid] > value:
            right = mid - 1
        elif input_array[mid] < value:
            left = mid + 1
            
        mid = (right + left)//2 

    else: 
        return - 1
test_list = random.sample(range(1,101),100)
print(test_list)
test_val1 = 25
test_val2 = 15
binary_search(test_list, test_val1)



@RunTime
def binary_search_rec(arr,x,l,r):
    mid = (r + l)//2
    if l <= r:
        
        if arr[mid] < x:
            # print(arr[l:r])
            return binary_search_rec(arr,x,mid + 1,r)
        if x  < arr[mid]:
            # print(mid )
            return binary_search_rec(arr,x,l,mid - 1)
        if x  == arr[mid]:
            # print(arr[l:r])
            return mid
    else:
        return - 1
test_list = 2
test_val1 = 25
test_val2 = 15
print (binary_search_rec(test_list, test_val2, 0, len(test_list)))
 