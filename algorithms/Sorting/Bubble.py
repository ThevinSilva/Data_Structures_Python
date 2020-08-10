import random 

#bubble sort algorithm
#space:
#   - O(log n) inplace

_list =random.sample(range(100),15)
print(_list)

def bubble(arr):
    n = len(arr)
    l = (n + 1) //2 
    for i in range(n):
        #pass
        print(' - ' * l + f' ~ {i + 1} ~ ' + ' - ' * l)
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1] , arr[j]
            print(arr)
    
bubble(_list)
