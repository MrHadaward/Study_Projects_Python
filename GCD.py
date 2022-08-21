# Objective of this project is to define a recursive function that finds the greatest commun divisor of two numbers  

def gcd(num1, num2):

    '''Takes two positive integers and find the greatest commun divisor'''

    if num1 % num2 == 0:
        return num2
    
    else:
        remainder = num1 % num2
        return gcd(num2, remainder)

num = gcd(8, 12)

print(num)
