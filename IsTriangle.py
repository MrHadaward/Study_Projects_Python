from ast import While
from os import remove

#Objective of this project is to check if three numbers can form a triangle


def is_triangle(a, b, c):
    '''Takes te positive numbers a, b and c and tests if they can form a triangle'''

    numbers = [a, b, c]
    minimun_value1 = min(numbers)
    minimun_value2 = min(numbers.remove(minimun_value1))
    max_value = max(numbers)

    if minimun_value1 + minimun_value2 >= max_value:
        print(f'os números {a}, {b} e {c} podem formar um triângulo !')
    
    else:
        print(f'os números {a}, {b} e {c} não podem formar um triângulo.')

# Take the input for the sides of the triangle and validate them

while True :
    a = input('Type the first side for the triangle: ')
    if a.isnumeric() == True:
        if float(a) >= 0:
            a = float(a)
            break

while True :
    b = input('Type the second side for the triangle: ')
    if b.isnumeric() == True:
        if float(b) >= 0:
            b = float(b)
            break

while True :
    c = input('Type the third side for the triangle: ')
    if c.isnumeric() == True:
        if float(c) >= 0:
            c = float(c)
            break

# Calls the function is_triangle to chech if the numbers can form a triangle

is_triangle(a, b, c)

