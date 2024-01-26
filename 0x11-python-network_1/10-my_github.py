#!/usr/bin/python3

"""
A python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import sys
import requests

if __name__ == '__main__':
    username = sys.argv[1]
    passtoken = sys.argv[2]
    url = 'https://api.github.com/user'
    header = {
        'Accept': 'application/vnd.github+json'
    }
    basicAuth = requests.auth.HTTPBasicAuth(username, passtoken)
    res = requests.get(url, auth=basicAuth, headers=header)
    print(res.json().get('id'))
