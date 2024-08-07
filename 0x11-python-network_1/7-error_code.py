#!/usr/bin/python3

"""
we are writting a script that takes in URL
and displays the body of response
"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
