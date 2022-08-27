import random

def histogram(a_str):

    ''' Takes a string and returns a histogram  '''
    
    a_dict = {}

    for char in a_str:
        if not char.isalpha():
            continue

        else:
            a_dict[char] = a_dict.get(char, 0) + 1
    
    return a_dict

def choose_from_histogram(a_dict):
    the_list = []

    for keys, vals in a_dict.items():
        for rep in range(vals):
            the_list.append(keys)

    return random.choice(the_list)
