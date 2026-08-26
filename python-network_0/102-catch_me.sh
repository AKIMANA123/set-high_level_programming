#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with "You got me!"
curl -s -X PUT -H "X-School-User-Id: 98" 0.0.0.0:5000/catch_me
