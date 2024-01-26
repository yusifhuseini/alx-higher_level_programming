#!/bin/bash
# A bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
if [ "$(curl -s -L -o /dev/null -w "%{http_code}" "$1")" = 200 ];then curl -s -L "$1"; fi
