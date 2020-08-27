import random
import heapq


#implement selection sort using a heap
def selection_sort(arr):
    temp = []
    heapq.heapify(arr)
    for i in range(len(arr)):
        temp.append(heapq.heappop(arr))
    return temp

if __name__ == '__main__':
    list_ = random.sample(range(100),10)
    print(list_)
    print(selection_sort(selection_sort(list_)))


