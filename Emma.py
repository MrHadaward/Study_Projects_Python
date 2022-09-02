
from operator import index
import random
import string

def emma_histogram():
    txt_file = open('Emma.txt', encoding='utf-8').read().replace('-', ' ').split()
    new_dict = {}

    for word in txt_file:
        word = word.strip(string.punctuation + string.whitespace + '?\'\",').lower()
        new_dict[word] = new_dict.get(word, 0) + 1
    
    return new_dict

def frequency(a_dict):
    new_list = []

    for key, value in a_dict.items():
        new_list.append((value, key))
    
    new_list.sort(reverse=True)

    return new_list

def most_frequent(a_list, top=20):
    for inde in range(top):
        print('{:^5} : {:^5}'.format(a_list[inde][1], a_list[inde][0]))

def random_word(hist):
    total = 0
    word_list = []
    total_list = []

    for key, val in hist.items():
        total += val
        word_list.append(key)
        total_list.append(total)
    
    rand_word = random.randint(1, total_list[-1])
    ind = None

    if rand_word >= total_list[(len(total_list) // 2)]:
        for num in total_list[(len(total_list) // 2):]:
            if rand_word <= num:
                ind = total_list.index(num)
                break
    
    else:
        for num in total_list[:(len(total_list) // 2)]:
            if rand_word <= num:
                ind = total_list.index(num)
                break
    
    print(word_list[ind])

random_word(emma_histogram())
