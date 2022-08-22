# Objective of this project is to check if a word is a palindrome

print(' ')

print('{0:^20}'.format('Is Palindrome ?'))
print('{0:^20}\n'.format('-' * 10))

# Takes the first word and validate it

while True:
    word1 = input('First word: ')
    if word1.isalpha():
        break

print(' ')

# Check wheter it is or not a palindrome

if word1 == word1[::-1]:
    print('{0:^20}'.format('PALINDROME !!'))

else:
    print('{0:^20}'.format('not palindrome.'))

print(' ')
