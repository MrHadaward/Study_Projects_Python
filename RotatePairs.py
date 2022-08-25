#Objective of this project is to find all rotate pairs in Words.txt

txt_file = open('Words.txt').read().split()

a_dict = {}

for words in txt_file:
    a_dict[words] = []

for words in a_dict:
    char = list(words)
    f = words

    for piece in char:
        char.insert(0, char[-1])
        del char[-1]
        var = ''.join(char) 
        
        if var == f:
            continue

        elif var in a_dict:
            a_dict[f] += [var]

for keys in a_dict:
    if a_dict[keys] != []:
        print(f'{keys} : {a_dict[keys]}')

            