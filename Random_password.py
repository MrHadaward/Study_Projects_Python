import random

print(' ')

while True:
    quantity = input('How many characters do you want ? ')
    if quantity.isnumeric() and int(quantity) - float(quantity) == 0:
        quantity = int(quantity)
        break

print(' ')

password = ''

for char in range(quantity):
    ran_char = random.randint(33, 126)
    password += chr(ran_char)

print(f'Your password is:   {password}')

print('')
