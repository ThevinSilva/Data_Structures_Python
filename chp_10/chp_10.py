#applications of a map in python 

test_string = """
fair, it was plausible. Even I thought that type of role suited her well.
Senjougahara was always sitting in a corner of the room, by herself,
reading a book. There were times when she would be reading an"""

def letter_count(seq):
    freq = dict()
    for i in seq.capitalize():
        if i.isalpha(): freq[i] = 1 + freq.get(i,0)
    return freq

def max_(dict_):
    max_k = ''
    max_v = 0
    for k , v in dict_.items():
        if v > max_v:
            max_k, max_v = k , v 
    return max_k , max_v 
print(max_(letter_count(test_string)))
print(max(letter_count(test_string).keys(), key = (lambda key : letter_count(test_string)[key])))

#hashing

#Cyclic-shift - bitwise opertors
def hash_code(s):
    mask = (1 << 32) - 1
    h = 0
    for i in s:
        h = (h << 5 & mask) | (h >> 27)
        h += ord(i)

print(2.0 == 2)
print(hash(2.3234))