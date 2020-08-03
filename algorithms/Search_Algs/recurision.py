def get_fib_list(position):
    """
    returns the fibonaci sequence until a given point
        :param position: 
    """
    if position <= 2:
        return [1,1]
    else:
        value = get_fib_list(position - 1)[-1] +  get_fib_list(position - 1)[-2]  
        return  get_fib_list(position -1) + [value] 

print(get_fib_list(11))

def get_fib(position):
    """
    returns the number that coresponds to the give position on the fibonaci sequence
        :param position: INT 
    """
    if position == 1 or position == 2: 
        return 1    
    else:
        return get_fib(position - 1) + get_fib(position - 2)
print(get_fib(11))