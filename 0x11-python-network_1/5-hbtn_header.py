#!/usr/bin/python3

"""
This script will displays the X-Request-Id header
variable of a request to a given variable
"""

# We import neccesary modules
import requests
import sys

# We check if the script is run directly
if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
