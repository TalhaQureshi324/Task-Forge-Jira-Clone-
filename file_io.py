import os

def read_file_lines(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def write_file_line(filename, line):
    with open(filename, 'a') as file:
        file.write(line + '\n')

def overwrite_file(filename, lines):
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')

def append_to_file(filename, line):
    with open(filename, 'a') as f:
        f.write(line + '\n')
