#!/bin/bash
# A bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -X DELETE -s -L "$1"
