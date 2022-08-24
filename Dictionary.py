def histogram(string):
    a_dict = {}

    for char in string:
        a_dict[char] = a_dict.get(char, 0) + 1
    
    print(a_dict)

histogram('arara')
