#!/usr/bin/python3

"""
We are going to displays the value of X-Request Id variable
that is found in the header of our response
"""

# we are going to check if the script is run directly
if __name__ == "__main__":
    # We are importing nessecary modules
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers["X-Request-Id"])
