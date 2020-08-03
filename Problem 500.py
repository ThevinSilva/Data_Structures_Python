import functools

def prime_factors(n):
    lst = []
    i = 2
    while i * i < n:
        if n % i:
            i += 1
        else:
            n //= i
            lst.append(i)
    if n > 1:
        lst.append(n)
    
    return {n:lst.count(n) for n in set(lst)}



count = 3
val = 0 
while val != 2e500500:
    val = functools.reduce(lambda x,y: x * y,map(lambda x: x + 1,prime_factors(count).values()))
    print(val, count)
    count += 1
else:
    print(val, count)