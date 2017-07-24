import random

def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
     #   P = random.randint(0, (N-1))
        A, P = Partition(A)
        Pivot = A[P]
        B = QuickSort(A[:P])
        C = QuickSort(A[P+1:])
        B.append(Pivot)
        array = B + C
        return array
    



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

# def readfile():
#     file = open("quiz.txt")
#     x = []
#     for line in file:
#         number = line.strip('\n')
#         no = int(number)
#         x.append(no)
#     return x

# x = readfile()

A = [3,1,5,4,6,8,9,4,6,0,3,2,1,5]
#N = 7
array = QuickSort(A)
print(array)