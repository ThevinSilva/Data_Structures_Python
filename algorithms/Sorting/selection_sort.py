import random
#selection sort
# time:
#   - best case: O(n^2)
#space:
#   - O(1) inplace
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1,len(arr)):
            #find the minimum
            if arr[min_idx] > arr[j]:
                min_idx = j
    arr[i] , arr[min_idx] = arr[min_idx] ,  arr[i] 



