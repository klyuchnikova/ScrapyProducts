import json
import sys
from os import path

if __name__ == "__main__" :
    file_path = path.join(path.dirname(sys.path[0]), "vprok.json")
    if not path.isfile(file_path):
        raise FileNotFoundError("the vprok.json file doesn't exist")
    with open(file_path, encoding='ascii') as f:
        data = json.load(f)
    print(data)