
from os import remove


def find_anagrams(a_dict):
    anagrams_dict = {}
    size_dict = {}

    for words in a_dict:
        size_dict[len(words)] = size_dict.get(len(words), []) + [words]

    for keys in a_dict:
        letters = ''.join(sorted(list(keys)))

        if  letters in anagrams_dict :
                print('-' * 10)
                continue
                
        for words in size_dict[len(letters)] :
            compare = ''.join(sorted(list(words)))
            
            if compare == letters :
                size_dict[len(letters)].remove(words)
                anagrams_dict[letters] = anagrams_dict.get(letters, []) + [words]
                print('0')
    
    a_list = []
    
    for values in anagrams_dict.values():
        a_list += [(len(values), values)]
    
    a_list.sort(reverse=True)

    for values in range(0,11):
        print(a_list[values])

txt_file = open('Words.txt').read().split()
a_dict = {}


for words in txt_file:
    a_dict[words] = None

find_anagrams(a_dict)
