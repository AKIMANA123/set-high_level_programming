#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using urllib"""

import urllib.request
import ssl


if __name__ == "__main__":
    # Create SSL context that doesn't verify certificates (for testing)
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url, context=ssl_context) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
