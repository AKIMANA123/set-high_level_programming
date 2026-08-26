#!/bin/bash
# Sends a JSON POST request with contents of a file and displays response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
