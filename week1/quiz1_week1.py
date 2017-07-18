def recurMult(number1, number2):
    
    if len(str(number1)) <= 1 or len(str(number2)) <=1:
        return number1*number2 
    
    else:  

        length = len(str(number1))
        middle = length/2

        p1 = int(number1 / 10**(middle))
        p2 = int(number1 % 10**(middle))
        p3 = int(number2 / 10**(middle))
        p4 = int(number2 % 10**(middle))

        a1 = recurMult(p1,p3)
        a2 = recurMult(p2,p4)
        a3 = recurMult((p1+p2),(p3+p4)) - a1 - a2

        answer = a1 * 10**(length) + a2 + a3*10**(middle)
        return answer


c = recurMult(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627)
print(c)