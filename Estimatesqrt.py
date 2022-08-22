# Objective of this project is to estimate the value of the sqrt of a using newton's method
# and compare with the true value.

import math


def estimatesqrt(a):
    epsilon = 0.0000000000001
    x = a / 2
    while True:
        
        y = (x + a/x) / 2
        
        if abs(y - x) <  epsilon :
            break
        x = y

    return x

def sqrttable(sqrt):
    print('a   my_sqrt(a)   math.sqrt(a)   diff')
    print('-   '  + '-' * len('my_sqrt(a)') + '   ' + '-' * len('math.sqrt(a)') + '   ' + '-' * len('diff'))

    for n in range(sqrt):
        g = estimatesqrt(n + 1)
        l = math.sqrt(n + 1)
        diff = abs(g - l)
        print(f'{n + 1:<3.1f} {g:-^12.5f} {l:^12.5f} {diff:>6.2f}')


# Print a table comparing the true sqrt's with the estimated ones

sqrttable(5)