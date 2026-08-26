#!/usr/bin/python3
"""Sends a POST request with a letter and handles JSON response"""

import requests
import sys


if __name__ == "__main__":
    # Get the letter from command line or set to empty string
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    # Send POST request with q parameter
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}
    response = requests.post(url, data=data)

    try:
        json_response = response.json()
        if json_response:
            id = json_response.get('id')
            name = json_response.get('name')
            print("[{}] {}".format(id, name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
