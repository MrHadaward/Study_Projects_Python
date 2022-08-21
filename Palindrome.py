# Objective of this project is to check if a word is a palindrome 

def is_palindrome(word):

    """Returns True if word is a palindrome."""
    
    if len(word) <= 1:
        return True
    
    if word[0] != word[-1]:
        return False
    
    return is_palindrome(word[1:-1])

while True :
    word = input('Type a word: ')

    if word.isalpha() :
        break

test = is_palindrome(word)

print(test)
