import sys
import os

# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)


def required(data, key_required=[]):
    for key in key_required:
        if key not in list(data.keys()):
            print(False)
            return False

    print(True)
    return True