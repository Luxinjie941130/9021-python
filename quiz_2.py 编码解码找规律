# Implements coding and decoding functions for pairs of integers.
# For coding, start at point (0, 0), move to point (1, 0), and turn
# around in an anticlockwise manner.
#
# Written by *** for COMP9021


from math import sqrt


def encode(a, b):
    if a == b == 0:
        n = 0
    elif a > 0 and b == 0:    
        n = 4 * a ** 2 - 3 * a
    elif a < 0 and b == 0:    
        n = 4 * a ** 2 - a
    elif b > 0 and a == 0:     
        n = 4 * b ** 2 - b
    elif b < 0 and a == 0:     
        n = 4 * b ** 2 - 3 * b
    elif a > 0 and b > 0 and  a > b: 
        n = 4 * a ** 2 - 3 * a + b
    elif b >= abs(a):                
        n = 4 * b ** 2 - b - a
    elif a < 0 and b > 0 and abs(a) > b:  
        n = 4 * a ** 2 - a - b
    elif a < 0 and b < 0 and a <= b:  
        n = 4 * a ** 2 - a -b
    elif a < 0 and b < 0 and a > b:  
        n = 4 * b ** 2 - 3 * b + a
    elif a > 0 and b < 0 and a <= abs(b) + 1: 
        n = 4 * b ** 2 - 3 * b + a
    elif a > 0 and b < 0 and a > abs(b) + 1: 
        n = 4 * a ** 2 - 3 * a + b     
    return n
    pass
    # Replace pass above with your code

    
def decode(n):
    i = 0
    while True:
        i += 1
        if n == 0:
            a = 0
            b = 0
            break
        elif sqrt(n) == int(sqrt(n)): 
            i = int(sqrt(n))
            if i % 2 == 0:          
                a = -(i // 2)
                b = -a
                break
            else:                   
                a = i // 2 + 1
                b = -(i //2)
                break
        elif i % 2 == 0 and n == i * (i + 1):  
            a = -(i // 2)
            b = a
            break
        elif i % 2 == 1 and n == i * (i + 1):  
            a = i // 2 + 1
            b = a
            break
        elif i % 2 == 1 and n > i**2 and n < i * (i + 1):   
            a = i // 2 + 1
            b = -(i //2) + (n - i**2)
            break
        elif i % 2 == 0 and n > i**2 and n < i * (i + 1):   
            a = -(i // 2)
            b = - a - (n - i**2)
            break
        elif i % 2 == 1 and n > i * (i + 1) and n < (i + 1)** 2: 
            b = i // 2 + 1
            a = b - (n - i * (i + 1))
            break
        elif i % 2 == 0 and n > i * (i + 1) and n < (i + 1)** 2: 
            b = -(i // 2)
            a = b + (n - i * (i + 1))
            break
    return (a ,b)
    pass
    # Replace pass above with your code
    

