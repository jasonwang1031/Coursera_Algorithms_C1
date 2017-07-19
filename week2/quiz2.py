global result

def mergesort(x):
    if len(x) <= 1:
        return x,0
    else:
        middle = int(len(x)/2)
        a,C1 = mergesort(x[:middle])
        b,C2 = mergesort(x[middle:])

        C3 = sortcount(a,b)
        c = merge(a,b)

        return c,(C1+C2+C3)


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

def sortcount(a,b):
    q = 0
    w = 0
    count = 0
    while q < len(a):
        while w <len(b):
            if a[q] > b[w]:
                count+= 1 
                w += 1
            else:
                w+=1
        w = 0
        q += 1
    return count


def readfile():
    file = open("file.txt")
    x = []
    for line in file:
        number = line.strip('\n')
        no = int(number)
        x.append(no)
    return x
    # while 1:
    #     line= file.readline()
    #     number = line.strip('\n')
    #     no = int(number)
    #     x.append(no)
    #     if not number:
    #         return x
    #         break
        


x = readfile()
c,count = mergesort(x)
print(count)