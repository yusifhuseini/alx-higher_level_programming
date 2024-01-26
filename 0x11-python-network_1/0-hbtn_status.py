#!/usr/bin/python3

"""
A python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

def fetch_url_content(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        return response.read()

def display_content_info(content):
    string = "Body response:\n" + f"\t- type: {type(content)}\n"
    string += f"\t- content: {content}\n"
    string += f"\t- utf8 content: {content.decode('utf-8')}"
    print(string)

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    
    try:
        content = fetch_url_content(url)
        display_content_info(content)
    except Exception as e:
        print(f"Error fetching URL content: {e}")

