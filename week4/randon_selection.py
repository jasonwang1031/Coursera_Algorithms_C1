import random

def RandomSelection(A,i):
    if len(A) <= 1:
        return (A[0])
    elif i > len(A):
        print ("Number not exits")
    else:
        A, P = Partition(A)
        if P == (i-1):
            return(A[P])
        elif P > (i-1):
            number = RandomSelection(A[:P],i)
        else:
            number = RandomSelection(A[P+1:],i-P-1)
    return number
    



def Partition(A):
    n = len(A)
    r = n-1
    p = random.randint(0, (n-1))
    j = 1
    i = 1
    A[0], A[p] = A[p], A[0]
    while j <= r:
        if A[j] < A[0]:
            A[i], A[j] = A[j], A[i]
            i+=1
            j+=1
        else:
            j+=1
    A[0],A[i-1] = A[i-1],A[0]
    
    return A,i-1


A =[1,2,3,4,5,6]
i = 2
print(RandomSelection(A,i))