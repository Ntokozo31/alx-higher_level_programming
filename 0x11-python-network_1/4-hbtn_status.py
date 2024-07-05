#!/usr/bin/python3

"""
Our script will fatch URL with request package
"""

# We import necessary modules
import requests

# We check if the script is run directly
if __name__ == "__main__":
    # We get our URL
    r = requests.get("https://alx-intranet.hbtn.io/status")
    t = r.text
    # Now it time to print
    print("Body response \n\t - type: {}\n\t - content: {}".format(type(t), t))
