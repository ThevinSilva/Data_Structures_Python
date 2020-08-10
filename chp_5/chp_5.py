import copy
#deep and shallow copy
list1 = [1,2,3,4,5]
list2 = list1 
list3 = copy.deepcopy(list1)
list2[3],list2[4] = list2[4],list2[3]
print(f'{"original":<10}:  {list1}')
print(f'{"shallow":<10}:  {list2}')
print(f'{"deep":<10}:  {list3}')

#compact arrays 
from array import array
arr = array('i',list1)
print(arr)

def caeser(txt,shift):
    alph = [chr(n) for n in range(97,123)]
    temp_lst = [None] * len(txt)
    for y,n in enumerate(list(txt)):
        if n.islower():
            temp_lst[y] = alph[(ord(n) - 97  + shift) % 26]
        if n.isupper():
            temp_lst[y] = alph[(ord(n) - 65   + shift) % 26].upper()
        if not n.isalnum():
            temp_lst[y] = n 
    return ''.join(temp_lst)
print(caeser('Kiss-shot-acerolion-heart-underblade',25))

class Caeser:
    def __init__(self,shift):
        '''
            ceaser shift
        '''
        self._shift = shift

    def _alph(self,shift = 0):
        return [chr(((n + shift)  %  26) + 97) for n in range(0,26)]

    def _transform(self,txt,lst):
        temp_lst = [None] * len(txt)
        for y,n in enumerate(list(txt)):
            if n.isalnum():
                if n.islower():
                    temp_lst[y] = lst[(ord(n) - 97) % 26]
                if n.isupper():
                    temp_lst[y] = lst[(ord(n) - 65) % 26].upper()
            else:
                temp_lst[y] = n
        return ''.join(temp_lst)

    def decode(self,txt):
        return self._transform(txt,self._alph()) 


    def encode(self,txt):
        return self._transform(txt,self._alph(self._shift)) 

foo = Caeser(25)
print(foo.encode('Kiss-shot-acerolion-heart-underblade'))

matrix = [[0] * 20 for n in range(20) ]
matrix[0][0] = 100
[print(n) for n in matrix]

