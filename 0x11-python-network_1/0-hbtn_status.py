#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    """Open a conn to the URL"""
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        """Read the res body as bytes"""
        html = response.read()
        """Decode the bytes to utf-8 str"""
        html_utf8 = html.decode('utf-8')
        """Print the body res"""
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html_utf8))
