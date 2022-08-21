# Objective of this project is define a recursive function that evaluete the ackermann function

def ackermann(m, n):

    ''' m and n are two positive integers.'''

    if m == 0:
        return n + 1
    
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)

    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n -1))

print(ackermann(3,4))
