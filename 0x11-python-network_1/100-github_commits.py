#!/usr/bin/python3
"""
This script lists 10 commits
(from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    res = requests.get(url)
    json = res.json()
    for i in range(10):
        commit = json[i].get('commit')
        sha = json[i].get('sha')
        author = commit.get('author').get('name')
        print("{}: {}".format(sha, author))
