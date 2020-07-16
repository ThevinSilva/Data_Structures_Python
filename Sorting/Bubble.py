import random 

#bubble sort algorithm 

_list = random.sample(range(100),15)
print(_list)

def bubble(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr   

print(bubble(_list))
