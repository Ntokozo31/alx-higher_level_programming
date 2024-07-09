#!/bin/bash
# Send a GET request to URL, display the body response

# Check if a URL was provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Define the URL from the first argument
URL="$1"

# Send the GET request with the specified header
curl -sH "X-HolbertonSchool-User-Id: 98" "$URL"
