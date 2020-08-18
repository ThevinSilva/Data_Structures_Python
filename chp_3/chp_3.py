
def disjoint(A,B,C):
    '''
        - check if there's an intersection in the three sequences that were inputed
    '''
    A , B , C = set(A),set(B), set(C)
    return True if len(A & B & C) == 0 else False

print(disjoint([1,2,3,4],[1,5,6],[1,2]))

def perms(seq):
    if len(seq) == 1:
        return [seq]
    result = []
    for x,y in enumerate(seq):
        result += [y + n for n in perms(seq[:x] + seq[x+1:])]
    return result 

print(perms('ABC'))
