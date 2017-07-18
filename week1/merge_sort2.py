def mergesort(x):
    if len(x) <= 1:
        return x
    else:
        middle = int(len(x)/2)
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        c = merge(a,b)
        return c

def merge(a,b):
    c = []
    while len(a) >0 and len(b)>0:
        if a[0] > b[0]:
            c.append(b[0])
            b.remove(b[0])
        else:
            c.append(a[0])
            a.remove(a[0])
    else:
        c += a
        c += b
    
    return c
    
x = [5,4,3,2,1]
c = mergesort(x)
print(c)