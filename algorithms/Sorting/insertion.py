import random
#insertion sort
# time:
#   - best case: O(n^2)
#space:
#   - O(log n) inplace
lst = [5,1,2,4,8] 

def insertion_sort(seq):
    for i in range(1,len(seq)):
        cur = seq[i]
        k = i
        while k > 0 and seq[k - 1] > cur:
            seq[k] = seq[ k - 1] 
            k -= 1
        seq[k] = cur
print(lst)
insertion_sort(lst)
print(lst)


