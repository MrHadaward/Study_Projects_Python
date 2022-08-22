# Objective of this project is to create a caesar cypher 97 122


print(' ')

print('{0:^40}'.format('Caesar Cypher'))
print('{0:^40}'.format('-' * len('Caesar Cypher')))

print(' ')

fine = False

# take the message and rotatio from the user and validate them

while not fine:
    fine = True
    while True:
        text = input('Write a message: ')
        if text.replace(' ', '').isalpha():
            text = text.lower()
            break
    
    while True:
        rot = input('Rotation: ')
        if rot.isnumeric() and int(rot) - float(rot) == 0:
            rot = int(rot) % 26
            break
    
    print(' ')
    
    new_text = ''
    
# change de old characters for the new rotated ones

    for char in text:
        if 97 <= ord(char) <= 122 or ord(char) == 32: 
    
            if char == ' ':
                new_text += ' '
    
            else:
                new_char = chr((ord(char) - 97 + rot) % 26 + 97)
                new_text += new_char
        else:
            fine = False
            print('Special character found type only normal characters !')
            print(' ')
            break
    
print('New message:', new_text)

print(' ')
