import os
import sys

def relative(module_name, relative):

    module = sys.modules[module_name]

    module_path = os.path.abspath(module.__file__)
    module_dir = os.path.dirname(module_path)

    return os.path.join(module_dir, relative)
