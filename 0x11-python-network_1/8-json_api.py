#!/usr/bin/python3

"""
A python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import sys
import requests

if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = f'http://0.0.0.0:5000/search_user'
    res = requests.post(url, data={'q': q})
    try:
        content = res.json()
        if content == {}:
            print("No result")
        else:
            print("[{}] {}".format(content.get('id'), content.get('name')))
    except Exception:
        print('Not a valid JSON')
