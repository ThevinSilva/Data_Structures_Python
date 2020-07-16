import random 
# quick sort algorithm 

def partition(arr,low,high):
    pivot = high
    border = low - 1

    for i in range(low,high):
        if arr[i] <= arr[pivot]:
            border += 1
            arr[border], arr[i] = arr[i], arr[border]
    arr[border + 1], arr[pivot] = arr[pivot], arr[border + 1]
    return border + 1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

_list = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(_list)
quick_sort(_list,0,len(_list) - 1)
print(_list)
    