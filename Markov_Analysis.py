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

def markov_analysis(a_list, preffix_lenght = 10):
    analysis = {}
    preffix_list = []
    rand_txt = []

    for rep in range((len(a_list)// preffix_lenght)):
        preffix = ' '.join(a_list[rep : (rep + preffix_lenght)])
        suffix = a_list[rep + preffix_lenght]

        analysis[preffix] = analysis.get(preffix, []) + [suffix]  

    for pre in analysis:
        preffix_list.append(pre)
    
    for rep in range(10):
        preffix = random.choice(preffix_list)
        suffix = random.choice(analysis[preffix])
        rand_txt.append(preffix)
        rand_txt.append(suffix)
    
    return ' '.join(rand_txt)

emma = open('Emma.txt', encoding='utf-8').read().replace('-', ' ').split()

print(markov_analysis(emma))
