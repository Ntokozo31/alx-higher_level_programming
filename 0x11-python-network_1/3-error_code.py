#!/usr/bin/python3

"""
Our script will take in a URL and send request and display it
the value of X-Request-Id variable found in the header
"""

# We import neccesary modules
from urllib import request, error
import sys

# We check if the script is run directly
if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            my_body = response.read()
            print(my_body.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
