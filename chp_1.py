import random
import time





#r-1.1

def is_multiple(n,m):
    i, val =1 , 0
    while val <= n:
        val = m*i
        i += 1 
        if val == n: return True  

print(is_multiple(12,3))

#r-1.2

def is_even(k):
    return True if int(str(k)[-1]) in (2,4,6,8,0) else False

print(is_even(177013))

#r-1.3

def minmax(seq):
    # challenge implement quick sort from memory
    return sorted(seq)[0], sorted(seq)[-1]

_list = random.sample(range(100),10)
print(_list)
print(minmax(_list))

#r-1.4 && 1.5
def sum_positive_nums(n):
    return sum([i ** 2 for i in range(1,n + 1)])

#r-1.5 && 1.6
def sum_positive_odd_nums(n):
    return sum([i ** 2 for i in range(1,n + 1) if i % 2 != 0])

#r-1.13
def reverse(seq):
    for n in range((len(seq))//2):
        seq[n], seq[-1 - n] = seq[-1 - n], seq[n] 
reverse(_list)
print(_list)

#r-1.15
def distinction(seq):
    x = len(set(seq))
    return True if x == len(seq) else False
print(distinction([2,2]))

#r-1.19
def alphabet():
    return [chr(n) for n in range(97,123)]
print(alphabet())

def factors(n):
    k = 1
    temp = []
    while k * k < n:
        if n % k == 0: 
            yield k
            temp.append(n // k)
        k+=1 
    if k * k == 0:
        yield k
    yield temp[::-1]


#projects
string = "cat"

# p-1.29  - print out every possible combination of this string

def perms(_str):
    if(len(_str)==1): return [_str]
    result=[]
    for i,v in enumerate(_str):
        result += [v+p for p in perms(_str[:i]+_str[i+1:])]
    return result

def perms1(_str):
    if len(_str) == 1: return [_str]
    result = []
    for x,y in enumerate(_str):
        result += [y + perms([_str[:x] + _str[x+1:]])]
    return result

print(perms(string))



#p-1.30  - write a Python program that can take a postitive integer greater than 2 as input and write out the number of times one must
#          repeatedly divide this number by 2 before getting a value less than 2

def foo(n):
    if n < 2:
        raise ValueError("please enter a value that is greater than 2")
    count = 0
    while not n < 2:
        n /= 2
        count += 1 
    return count , n

print(foo(30))

#P-1.34    - A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone program that will write out the
#            following sentence one hundred times: “I will never spam my friends
#            again.” Your program should number each of the sentences and it should
#            make eight different random-looking typos.

def spam():
    rand_ints = random.sample(range(100),10)
    alphabet = [chr(n) for n in range(97,123)]
    print(alphabet)
    for i in range(100):
        string = f'{i} I will never spam my friend again'
        if i in rand_ints:
            string = string.replace(alphabet[random.randint(0,len(alphabet) - 1)], alphabet[random.randint(0,len(alphabet) - 1)])
        print(string)
spam()

