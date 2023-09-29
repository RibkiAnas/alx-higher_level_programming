#!/usr/bin/python3
"""
This script takes in a URL, sends a request
to the URL and displays the body of the
response, while checking for HTTP status
codes greater than or equal to 400.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    status_code = res.status_code
    if status_code < 400:
        print(res.text)
    else:
        print("Error code: {}".format(status_code))
