#!/usr/bin/python3

"""
A python script that list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails” using the GitHub API
"""

import sys
import requests

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    header = {'Accept': 'application/vnd.github+json'}
    res = requests.get(url, headers=header)
    commits = res.json()[:10]
    for commit in commits:
        print('{}: {}'.format(
            commit['sha'], commit['commit']['author']['name'])
        )
