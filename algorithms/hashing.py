import random
"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""
class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        key = self.calculate_hash_value(string)
        if self.table[key] == None:
            self.table[key] = key
            return "stored" 
        else: 
            return "taken"

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        key = string.calculate_hash_value(string)
        if self.table[key] != None:
            return self.table[key]
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        return sum([ord(y)*(10**(2-(2*x))) for x,y in enumerate(string[:2])]) 
    
# Setup
# hash_table = HashTable()

# # Test calculate_hash_value
# # Should be 8568
# # print (hash_table.calculate_hash_value('UDACITY'))

# # # Test lookup edge case
# # # Should be -1
# print( hash_table.lookup('UDACITY'))

# # # Test store
# hash_table.store('UDACITY')
# # # Should be 8568
# print( hash_table.lookup('UDACITY'))

# # # Test store edge case
# hash_table.store('UDACIOUS')
# # # Should be 8568
# print( hash_table.lookup('UDACIOUS'))

# l = ['sat', 'bat', 'cat', 'mat'] 

# print(list(map(lambda x: [n for n in x],l)))

def partition(arr,low,high):
    border = low - 1
    pivot = arr[high]

    for i in range(low,high):
        if arr[i] <= pivot:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
    arr[high], arr[border + 1] = arr[border + 1], arr[high]
    return border + 1

def quicksort(arr,low,high):
    if low < high:
        p = partition(arr,low,high)
        quicksort(arr,low,p - 1)
        quicksort(arr,p + 1,high)

_list = random.sample(range(100),10)
print(_list)
quicksort(_list,0,len(_list) - 1) 
print(_list)