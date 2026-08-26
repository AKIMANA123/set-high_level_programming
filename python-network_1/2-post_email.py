#!/usr/bin/python3
"""Sends a POST request with email parameter and displays response body"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Create a POST request
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        # Read and decode the response body
        content = response.read().decode('utf-8')
        print(content)
