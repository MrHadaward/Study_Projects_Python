# Objective of this project is to play with dictionary


# Checks if there are duplicates in a list

def has_duplicates(a_list):
    a_dict = {}

    for element in a_list:
        a_dict[element] = a_dict.get(element, 0) + 1

        if a_dict[element] >= 2:
            return True
    
    return False


#inverts a dictionary

def invert_dict(a_dict):
    new_dict = {}
    for keys in a_dict:
        new_dict[a_dict[keys]] = new_dict.get(a_dict[keys], []) + [keys]
        
    
    print(new_dict)

def histogram(string):
    a_dict = {}

    for char in string:
        a_dict[char] = a_dict.get(char, 0) + 1
    
    print(a_dict)
    return a_dict

invert_dict(histogram('ararabb'))
print(has_duplicates(['arara', 'bird', 'gato', 'pato']))
