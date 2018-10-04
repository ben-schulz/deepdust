import os
import sys

def relative(module_name, relative):

    module = sys.modules[module_name]

    module_path = os.path.abspath(module.__file__)
    module_dir = os.path.dirname(module_path)

    return os.path.join(module_dir, relative)


def clean_directory(path_to_clean):

    try:
        os.mkdir(path_to_clean)

    except FileExistsError:

        files = os.listdir(path_to_clean)
        for f in files:
            filepath = os.path.join(path_to_clean, f)
            os.remove(filepath)

        os.rmdir(path_to_clean)
        os.mkdir(path_to_clean)

