import random
#insertion sort
# time:
#   - best case: O(n^2)
#space:
#   - O(1) inplace
lst = [5,1,2,4,8] 

def insertion_sort(seq):
    for i in range(1,len(seq)):
        cur = seq[i]
        j = i
        while j > 0 and cur < seq[j - 1]:
            seq[j] = seq[j - 1]
            j -= 1
        seq[j] = cur
print(lst)
insertion_sort(lst)
print(lst)


