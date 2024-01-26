#!/bin/bash
# A bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -I "$1" | grep -i "Allow" | sed -E 's/Allow:(\s)*//I'
