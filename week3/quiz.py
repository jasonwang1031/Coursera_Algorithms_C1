import random

def partition(arr, l, r, i, count=None, asserting=False):
    if asserting: assert l <= i <= r
    p = arr[int(i)]                            
    arr[int(l)], arr[int(i)] = arr[int(i)], arr[int(l)]         
    i = l + 1                               
    for j in range(i, r + 1):
        if count: count(1)               
        if arr[j] < p:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1                               
    i -= 1
    arr[l], arr[i] = arr[i], arr[l]       
    if asserting: assert all(x < p for x in arr[l:i])
    if asserting: assert all(x >= p for x in arr[i+1:r])
    return i


rand = lambda arr, l, r: randint(l, r)

def quicksort(arr, l=0, r=None, count=None, pivot=rand):
    if r is None: r = len(arr) - 1
    if r - l < 1: return
    i = pivot(arr, l, r)
    i = partition(arr, l, r, i, count)
    quicksort(arr, l, i - 1, count, pivot)
    quicksort(arr, i + 1, r, count, pivot)


# The following are pivot choice methods - you can use these to 
# in `quicksort` to choose a particular element on which to pivot.

def first(arr, l, r): return l

def last(arr, l, r): return r

def median(arr, l, r):

    m = 0 if (r - l) == 1 else ((r - l)) / 2 + l
    M = arr[int(m)]                      # middle element
    L = arr[int(l)]                      # leftmost element
    R = arr[int(r)]                      # rightmost element
    ordered = sorted([(L, l), (M, m), (R, r)])
    return ordered[1][1]            # index of median of the three


class Counter:

    def __init__(self, n=0):
        self.total = n

    def __call__(self, x=0):
        self.total += x


if __name__ == '__main__':

    input = [int(x.rstrip()) for x in open('quiz.txt')]

    for pivot in [first, last, median]:
        arr = input[:]
        count = Counter()
        quicksort(arr, count=count, pivot=pivot)
        assert arr == sorted(input)
        print (pivot.__name__, count.total)


# find the code online/ self-studied it, and implemented to my quiz 