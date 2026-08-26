#!/bin/bash
# Script that takes a URL, sends a GET request, and displays the body of a 200 status code response
curl -s -f -L "$1"
