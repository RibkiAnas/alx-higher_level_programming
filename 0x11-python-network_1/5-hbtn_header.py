#!/usr/bin/python3
"""
This script that takes in a URL, sends a
request to the URL and displays the value
of the variable X-Request-Id in the
response header
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    headers = res.headers
    x_request_id = headers.get('X-Request-Id')
    print(x_request_id)
