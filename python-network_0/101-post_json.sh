#!/bin/bash
# Script that sends a JSON POST request with the contents of a file

if ! jq . "$2" > /dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 0
fi

curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
