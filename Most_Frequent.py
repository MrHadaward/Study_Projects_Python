
# Objective os this project is to find the most frequent letters in a text

def most_frequent(string):
    one_dict = {}
    l_string = string.lower()
    
    for char in l_string:
        if not char.isalpha():
            continue

        else:
            one_dict[char] = one_dict.get(char, 0) + 1
    
    rev_dict = {}
    for keys, values in one_dict.items():
        rev_dict[values] = rev_dict.get(values, []) + [keys]
    
    seq = sorted(rev_dict)

    for elements in seq[::-1]:
        for letters in rev_dict[elements]:
            print(f'{letters} : {elements}')


most_frequent('''Lists, dictionaries and tuples are examples of data structures; in this chapter we are starting to see compound data structures, like lists of tuples, or dictionaries that con‐
tain tuples as keys and lists as values. Compound data structures are useful, but they
are prone to what I call shape errors; that is, errors caused when a data structure has
the wrong type, size, or structure. For example, if you are expecting a list with one
integer and I give you a plain old integer (not in a list), it won’t work''')
