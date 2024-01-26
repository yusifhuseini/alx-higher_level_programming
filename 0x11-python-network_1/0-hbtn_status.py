#!/usr/bin/python3

import urllib.request

def fetch_url(url):
    """
    Fetches the content of the given URL.

    Args:
    - url (str): The URL to fetch.

    Returns:
    - bytes: The content of the URL.
    """
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        content = response.read()
    return content

def print_content_info(content):
    """
    Prints information about the content.

    Args:
    - content (bytes): The content to print information about.
    """
    string = "Body response:\n" + f"\t- type: {type(content)}\n"
    string += f"\t- content: {content}\n"
    string += f"\t- utf8 content: {content.decode('utf-8')}"
    print(string)

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    
    # Fetch content
    content = fetch_url(url)

    # Print content information
    print_content_info(content)
