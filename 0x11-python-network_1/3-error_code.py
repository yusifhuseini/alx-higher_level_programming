#!/usr/bin/python3

"""
A python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response (decoded in utf-8)
"""

import sys
import urllib
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
