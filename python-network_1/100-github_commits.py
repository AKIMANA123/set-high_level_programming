#!/usr/bin/python3
"""Lists 10 most recent commits of a GitHub repository"""

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    params = {'per_page': 10}
    response = requests.get(url, params=params)

    commits = response.json()
    for commit in commits:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author_name))
