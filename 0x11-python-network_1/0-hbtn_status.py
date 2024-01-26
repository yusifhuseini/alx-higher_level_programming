#!/usr/bin/python3

"""
A python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request
from urllib.error import URLError, HTTPError

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            content = response.read()
            string = "Body response:\n" + f"\t- type: {type(content)}\n"
            string += f"\t- content: {content}\n"
            string += f"\t- utf8 content: {content.decode('utf-8')}"
            print(string)
    except HTTPError as e:
        print(f"HTTPError: {e.code}")
    except URLError as e:
        print(f"URLError: {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
