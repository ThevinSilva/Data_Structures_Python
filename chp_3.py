
def disjoint(A,B,C):
    '''
        - check if there's an intersection in the three sequences that were inputed
    '''
    A , B , C = set(A),set(B), set(C)
    return True if len(A & B & C) == 0 else False

print(disjoint([1,2,3,4],[1,5,6],[1,2]))

# import matplotlib.pyplot as plt
# import numpy as np

# # 100 linearly spaced numbers
# x = np.linspace(-5,5,100)

# # the function, which is y = x^2 here
# y = x**2

# # setting the axes at the centre
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.spines['left'].set_position('center')
# ax.spines['bottom'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')

# # plot the function
# plt.plot(x,y, 'r')

# # show the plot
# plt.show()

def perms(seq):
    if len(seq) == 1:
        return [seq]
    result = []
    for x,y in enumerate(seq):
        result += [y + n for n in perms(seq[:x] + seq[x+1:])]
    return result 
        

print(perms('ABC'))
