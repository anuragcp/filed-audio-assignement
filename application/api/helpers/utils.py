import sys
import os

# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)


def required(data, key_list=[]):
    if data.keys() == key_list:
        return True
    else:
        return False