#!/bin/bash
# Makes a request to cause response body to contain 'You got me!'
curl -sL -X PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me
