import random

def QuickSort(A, N):
    if N <= 1:
        return A
    else:
        P = random.randint(0, (N-1))
        A = Partition(A,P)
        B = QuickSort(A[:P], len(A[:P]))
        C = QuickSort(A[P:],len(A[P:]))
        array = B + C
        return array
    



def Partition(A, P):
    r = len(A)-1
    j = 1
    i = 1
    A[0], A[P] = A[P], A[0]
    while j <= r:
        if A[j] < A[0]:
            A[i], A[j] = A[j], A[i]
            i+=1
            j+=1
        else:
            j+=1
    A[0],A[i-1] = A[i-1],A[0]
    return A


A = [3,1,5,4,6,8,9]
N = 7
array = QuickSort(A,N)
print(array)