
# Objective of this project is to check fermat last theorem by
# taking three inputs of the user.


print(' ' * 15 + "-" * 50)
print('Fermat\'s Last Theorem says that there are no positive integers a, b, and c such that:\n')
print(' ' * 30 + 'a^n + b^n = c^n\n')
print(' ' * 20 + 'for any values of n greater than 2.')
print(' ' * 15 + "-" * 50 + '\n' )

print('Let\'s test it. \n')

# Takes inputs for the numbers a,b and c of fermat last theorem and validate them

while True :
    a = input('Type a positive integer for "a": ')
    if a.isnumeric() == True:
        if int(a) - float(a) == 0:
            a = int(a)
            break

print(' ')

while True:
    b = input('Type a positive integer for "b": ')
    if b.isnumeric() == True:
        if int(b) - float(b) == 0:
            b = int(b)
            break

print(' ')

while True:
    c = input('Type a positive integer for "c": ')
    if c.isnumeric() == True:
        if int(c) - float(c) == 0:
            c = int(c)
            break

print(' ')

# Takes an input for the number n and validate

while True:
    n = input('Type any number greater than 2 for "n": ')
    if n.isnumeric() == True:
        if float(n) > float(2):
            n = float(n)
            break

print(' ')

print(f'O resultado de {a}^{n} + {b}^{n} = {c}^{n} é: \n')
print(f'{a**n + b**n} = {c**n}')

print(' ')

print('E fermat estava certo.')

print(' ')

