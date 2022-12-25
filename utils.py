import os
import pprint
from typing import List


def reverse_mapping(dictionary: dict) -> dict:
    """Swaps and retruns keys for values and vice versa of a dictionary. 

    Args:
        *dictionary: A Python dictionary with boths keys and values as unique strings.

    Returns:
        A Python dictionary with 'dictionary' keys as values and 'dictionary' values as keys.
    """

    reversed_dict = dict([(v, k) for k, v in dictionary.items()])
    return reversed_dict


def create_folder(folder_path: str) -> None:
    """Creates folder(s) specified by by a folder path.

    Used in 'postwritten_scripter.py' and 'prewritten_scripter.py'.
    
    Args:
        *folder_path: A str containing the path to be created.
    """

    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)


def list_files(folder_path: str) -> dict:
    """Lists files in a directory.

    Used in 'script_executor.py', 'postwritten_scripter.py', and 'prewritten_scripter.py'.
    
    Args:
        *folder_path: A str containing the path to be listed from.

    Returns:
        A dict with the numbers and the filenames by order of time of creation.
    """

    dir_list = os.listdir(folder_path)
    num_of_files = len(dir_list)
    filenames = {k: dir_list[k] for k in range(num_of_files)}

    return filenames


def string_stripper(string: str, strip_list: tuple) -> str:
    """Removes a string of characters from a string.

    Used in 'keyboard_inputter.py', 'state_manager.py', and 'prewritten_scripter.py'.
    
    Args:
        *string: The str from which characters are to be removed from.
        *strip_list: A tuple of strings to be removed(stripped) from'string'.
        
    Returns:
        A str after it has been stripped."""

    stripped_str = string
    for s in strip_list:
        stripped_str = stripped_str.replace(s, "")

    return stripped_str


def write_file(filename: str, file_contents: List[str], folder_path: str) -> None:
    """Writes to a .txt file specified by the folder path and filename.

    Used in 'postwritten_scripter.py' and 'prewritten_scripter.py'.
    
    Args:
        *filename: A str containing the name of the file.
        *file_contents: A list of str to be stored in the .txt file.
        *folder_path: A str having the path that the .txt file is to be stored.
    """
    file_path = fr"{folder_path}/{filename}.txt"

    with open(file_path, "w") as f:
        f.writelines(file_contents)

def printer(obj) -> None:
    """Pretty prints an object.

    Used in 'script_executor.py', 'prewritten_scripter.py', and 'postwritten_scripter.py'.
    
    Args:
        *obj: A object to be pretty printed. Could be a str, list, tuple, or dict.
    """
    print()
    pprint.pp(obj)
    print()
