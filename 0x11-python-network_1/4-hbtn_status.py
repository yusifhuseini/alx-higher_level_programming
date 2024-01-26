#!/usr/bin/python3

"""
A python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import requests
    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    print("Body response:\n\t- type: {}\n\t- content: {}".format(
        type(res.text), res.text)
    )
