#!/usr/bin/python3

# We are importing necessary modules
import requests
import sys

# We check if the script is run directly
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
