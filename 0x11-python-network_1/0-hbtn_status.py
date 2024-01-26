#!/usr/bin/python3

"""
A python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

def fetch_url_content(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        content = response.read()
    return content

def print_content_info(content):
    string = "Body response:\n" + f"\t- type: {type(content)}\n"
    string = string + f"\t- content: {content}\n"
    string = string + f"\t- utf8 content: {content.decode('utf-8')}"
    print(string)

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    
    # Fetch URL content
    page_content = fetch_url_content(url)
    
    # Print information about the content
    print_content_info(page_content)
