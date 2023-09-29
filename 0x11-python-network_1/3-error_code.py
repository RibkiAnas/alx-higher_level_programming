#!/usr/bin/python3
"""
This script that takes in a URL, sends a
request to the URL and displays the body
of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            html_utf8 = html.decode('utf-8')
            print(html_utf8)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
