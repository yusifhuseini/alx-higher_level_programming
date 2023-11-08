#!/usr/bin/python3

"""
A module: Defines a function that appends a
new text after each line containing the search text
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing a specific string

    Args:
        search_string (str): search text
        new_string (str): new text
    """
    content = ""
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            content += line
            if search_string in line:
                content += new_string

    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(content)
