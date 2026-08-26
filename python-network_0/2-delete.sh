#!/bin/bash
# Script that sends a DELETE request to the URL passed as first argument and displays the body
curl -s -X DELETE "$1"
