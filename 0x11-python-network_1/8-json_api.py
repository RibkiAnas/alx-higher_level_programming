#!/usr/bin/python3
"""
This script that takes in a letter and
sends a POST request to
http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': letter}
    url = 'http://0.0.0.0:5000/search_user'
    res = requests.post(url, data=data)
    try:
        json = res.json()
        if not json:
            print("No result")
        else:
            id = json.get("id")
            name = json.get("name")
            print("[{}] {}".format(id, name))
    except ValueError:
        print("Not a valid JSON")
