# Objective of this project is to take a list of lists with numbers and sum them

from hashlib import new


print(' ')

def has_duplicates(a_list):
    the_last_element = ''

    for element in a_list:
        if str(element) == the_last_element:
            return True
        
        else:
            the_last_element = ''
            the_last_element += str(element)
    
    return False

def is_anagram(word1, word2):

    '''Checks if two words are anagrams'''

    word1 = list(word1)
    word2 = list(word2)
    
    if sorted(word1) == sorted(word2):
        return True
    
    else:
        return False

def is_sorted(a_list):

    '''Checks wheter a list is sorted or not'''

    if a_list  == sorted(a_list):
        return True
    
    else:
        return False

def chop(a_list):

    '''Delete the first and last element of a list'''

    if len(a_list) == 0:
        pass

    elif len(a_list) == 1:
        del a_list[0]

    else:
        del a_list[0]
        del a_list[-1]

def middle(a_list):

    '''Takes a list and separate the middle elements of the firts and last one'''

    if len(a_list) <= 2:
        print('There is no middle element')
    
    else:
        print(a_list[1:-1])

def cumsum(a_list):
    a_accumulator = 0
    new_list = []

    for elements in a_list:
        a_accumulator += elements
        new_list.append(a_accumulator)
    
    print(new_list)

def nested_sum(a_list):

    '''Takes a nested list with lists of numbers and sum them'''

    the_sum = 0

    for elements in a_list:
        the_sum += sum(elements)
    
    print(the_sum)

one_list = [[1, 3], [1]]
another_list = [1, 2, 3, 4, 5]
more_lists = [4, 3, 2]
test = [1, 2]

nested_sum(one_list)
cumsum(another_list)
middle(another_list)
chop(another_list)
print(another_list)
print(is_sorted(more_lists))
print(is_anagram('arara', 'raraaa'))
print(has_duplicates(test))

print(' ')
