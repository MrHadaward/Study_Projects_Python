def new_file(look, repl, file1, file2):
    file_read = open(file1, encoding='utf-8').read().replace(look, repl)
    new_one = open(file2, 'w', encoding='utf-8').write(file_read)

    return new_one

new_file('to', 'xxxxx', 'Emma.txt', 'New_Emma.txt')
