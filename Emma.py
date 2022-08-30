
import string

def emma_histogram():
    txt_file = open('Emma.txt', encoding='utf-8').read().replace('-', ' ').replace('"', '').split()
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


x = 20

print('{:-^{space}}'.format('Bubble', space = x))

n = ['12', '+', '1']
print(eval('abs + gds'))