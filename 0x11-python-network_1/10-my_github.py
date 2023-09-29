#!/usr/bin/python3
"""
This script takes your GitHub credentials
(username and password) and uses the GitHub
API to display your id.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    auth = {'username': username, 'password': password}
    url = 'https://api.github.com/user'
    res = requests.get(url, auth=auth)
    try:
        json = res.json()
        user_id = json.get('id')
        print(user_id)
    except ValueError:
        print(None)
