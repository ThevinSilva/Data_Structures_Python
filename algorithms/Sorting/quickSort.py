import random
#quick sort
# time:
#   - best case: O(log n)
#   - worst case: O(n^2)
#space:
#   - O(log n) inplace
def partition(arr,low,high):
    pivot = high
    border = low - 1

    for i in range(low,high):
        if arr[i] <= arr[pivot]:
            border += 1
            arr[border], arr[i] = arr[i], arr[border]
    print(arr)
    arr[border + 1], arr[pivot] = arr[pivot], arr[border + 1]
    return border + 1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

def quick_sort_interface(_list):
    quick_sort(_list,0,len(_list) - 1)


_list = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(_list)
quick_sort_interface(_list)
print(_list)
print([n for n in range(100,20,-1)])