#!/usr/bin/python3

"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

def fetch_url_content(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        content = response.read()
    return content

def format_content(content):
    string = "Body response:\n" + f"\t- type: {type(content)}\n"
    string = string + f"\t- content: {content}\n"
    string = string + f"\t- utf8 content: {content.decode('utf-8')}"
    return string

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    
    content = fetch_url_content(url)
    formatted_string = format_content(content)
    
    print(formatted_string)
