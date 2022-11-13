import os
import pprint

def reverse_mapping(dictionary):
    reversed_dict = dict([(v, k) for k, v in dictionary.items()])
    return reversed_dict


def create_folder(folder_path):
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)


def list_files(folder_path):
    dir_list = os.listdir(folder_path)
    num_of_files = len(dir_list)
    filenames = {k: dir_list[k] for k in range(num_of_files)}

    return filenames


def printer(obj):
    print()
    pprint.pp(obj)
    print()
