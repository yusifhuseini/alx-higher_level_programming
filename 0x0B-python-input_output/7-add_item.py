#!/usr/bin/python3

"""
A script: Adds all arguments to a Python list, and then save them to a file
"""

"""Import argument vector"""
argv = __import__('sys').argv

"""Import function to save to a json file"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

"""Import function to load from json file"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def script(argv):
    """
    Appends elements in argument vector to a json file (`add_item.json`)

    Args:
        argv (list): list of arguments pass into the script

    Raises:
        Exception: if the file `add_item.json` is empty
    """
    try:
        line = load_from_json_file('add_item.json')
    except Exception:
        line = []
    for v in argv:
        line.append(v)
    save_to_json_file(line, 'add_item.json')


if __name__ == '__main__':
    script(argv[1:])
