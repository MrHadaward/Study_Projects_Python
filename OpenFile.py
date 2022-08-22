fin = open('Words.txt')
words = fin.read().split()

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

is_abecedarian(words)