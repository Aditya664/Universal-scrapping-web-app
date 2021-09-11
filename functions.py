import os


def create_directory(folder_namr):
    if not os.path.exists(folder_namr):
        os.makedirs(folder_namr)


def create_new_file(path):
    f = open(path, 'w')
    f.write("")
    f.close()


def write_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


def clean_file(path):
    f = open(path, 'w')
    f.close()


def does_file_exists(path):
    return os.path.isfile(path)


def read_data(path):
    with open(path, 'rt') as file:
        for line in file:
            print(line)
