import os
import pprint

"""A module that contains all utilities functions

Functions
---------
    reverse_mapping:
"""


def reverse_mapping(dictionary: dict) -> dict:
    """Swaps and retruns keys for values and vice versa of a dictionary.

    Args:
        dictionary: A Python dictionary with boths keys and values as unique strings.

    Returns:
        reversed_dict: A Python dictionary with 'dictionary' keys as values and 'dictionary' values as keys."""

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


def string_stripper(string, strip_list):
    stripped_str = string
    for s in strip_list:
        stripped_str = stripped_str.replace(s, "")

    return stripped_str


def printer(obj):
    print()
    pprint.pp(obj)
    print()
