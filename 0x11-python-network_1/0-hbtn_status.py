#!/usr/bin/python3

"""
A python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        string = "Body response:\n" + f"\t- type: {type(content)}\n"
        string = string + f"\t- content: {content}\n"
        string = string + f"\t- utf8 content: {content.decode('utf-8')}"
        print(string)
