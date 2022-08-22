# Objective of this project is to define some functions to filter this word list

fin = open('Words.txt')
words = fin.read().split()

# checks wheter a word is ou not abcedarian

def is_abecedarian(words):
    for word in words:
        notis = False
        cod = 0

        for letter in word:
            if ord(letter) < cod:
                notis = True
                break

            cod = ord(letter)
    
        if notis:
            pass

        else:
            print(word)


# checks if a word uses all given letters

def uses_all(words, lette):
    for word in words:
        nothas = False

        for letter in lette:
            if letter not in word:
                nothas = True
                break
    
        if nothas:
            pass

        else:
            print(word)


# cheks if a word uses only the given letters 

def uses_only(words, lette):
    for word in words:
        nothas = False

        for letter in word:
            if letter not in lette:
                nothas = True
                break
    
        if nothas:
            pass

        else:
            print(word)

# checks if a word contain a forbidden letter provided

def avoids(words, forbidden):
    for word in words:
        has = False

        for letter in word:
            if letter in forbidden:
                has = True
                break
    
        if has:
            pass

        else:
            print(word)
