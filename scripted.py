import os.path


def folder_exists(folder_path):
    if os.path.exists(folder_path):
        return True

    return False




