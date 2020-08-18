import random
#insertion sort
# time:
#   - best case: O(n^2)
#space:
#   - O(log n) inplace
lst = [5,1,2,4,8] 

def insertion_sort(seq):
    for i in range(1,len(seq)):
        k = i
        while k > 0 and  seq[k] > seq[i]:
            seq[k] = seq[]
            k -=  
print(lst)
insertion_sort(lst)
print(lst)


