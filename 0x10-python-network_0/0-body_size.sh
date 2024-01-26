#!/bin/bash
# A bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -L -I "$1" | grep -i "content-length" | sed -E 's/content-length:(\s)*//I'
