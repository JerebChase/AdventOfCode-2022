import re

def handle_input(input_line, directory, current):
    if input_line.startswith('$ cd'):
        directory, current = handle_cd(input_line.split()[2], directory, current)
    elif input_line.startswith('dir'):
        directory = handle_dir(input_line.split()[1], directory, current)
    elif bool(re.search('\d+\s\w+', input_line)):
        directory = handle_file(input_line.split()[0], directory, current)
    return directory, current

def handle_cd(current_dir, directory, current):
    if current_dir == '/':
        current = 0
    elif current_dir == '..':
        current = directory[current]['parent']
    else:
        item = [elem for elem in directory if elem['dir'] == current_dir and elem['parent'] == current][0]
        current = directory.index(item)
    return directory, current

def handle_dir(listed_dir, directory, current):
    directory.append({'dir': listed_dir, 'parent': current, 'size': 0})
    return directory

def handle_file(file_size, directory, current):
    directory = update_dir_size(file_size, current, directory)
    return directory

def update_dir_size(file_size, index, directory):
    directory[index]['size'] += int(file_size)
    if directory[index]['parent'] is None:
        return directory
    else:
        return update_dir_size(file_size, directory[index]['parent'], directory)

def get_size(item):
    return item['size']

def get_delete_dir_size(dir_input):
    directory = [{'dir': '/', 'parent': None, 'size': 0}]
    current = 0
    small_dir_sum = 0
    for i in range(len(dir_input)):
        directory, current = handle_input(dir_input[i].strip(), directory, current)
    directory.sort(key=get_size)
    small_dirs = filter(lambda item: item['size'] <= 100000, directory)
    for small_dir in small_dirs:
        small_dir_sum += small_dir['size']
    return small_dir_sum

def get_dir_to_delete(dir_input):
    directory = [{'dir': '/', 'parent': None, 'size': 0}]
    current = 0
    smallest_big_dir = 70000000
    for i in range(len(dir_input)):
        directory, current = handle_input(dir_input[i].strip(), directory, current)
    available_space = 70000000 - directory[0]['size']
    big_dirs = filter(lambda item: item['size'] >= 30000000 - available_space, directory)
    for big_dir in big_dirs:
        if big_dir['size'] < smallest_big_dir:
            smallest_big_dir = big_dir['size']
    return smallest_big_dir
