#!/usr/bin/python3

"""
Our script wil take in URL and email address and sends a post
request to the paste URL with the email as a parameter
then finally displays the body of response
"""

# We import necessary modules
import requests
import sys

# We check if the script is run directly
if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
