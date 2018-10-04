import os
import sys

def relative(module_name, relative):

    module = sys.modules[module_name]

    module_path = os.path.abspath(module.__file__)
    module_dir = os.path.dirname(module_path)

    return os.path.join(module_dir, relative)


def clean_directory(relative_path):
    """
    clean and recreate a directory
    relative to this project path
    (because allowing other paths
    to this function would be dangerous)
    """    

    this_path = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_path)
    base_path = os.path.join(this_dir, '..')

    path_to_clean = os.path.join(base_path, relative_path)

    try:
        os.mkdir(path_to_clean)

    except FileExistsError:

        files = os.scandir(path_to_clean)
        for f in files:
            os.remove(f.path)

        os.rmdir(path_to_clean)
        os.mkdir(path_to_clean)

