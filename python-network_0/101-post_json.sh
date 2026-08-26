#!/bin/bash
# Sends a JSON POST request with contents of a file and displays response
jq . "$2" > /dev/null 2>&1 && curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1" || echo "Not a valid JSON"
