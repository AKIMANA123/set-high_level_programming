#!/bin/bash
jq . "$2" > /dev/null 2>&1 && curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1" || echo "Not a valid JSON"
