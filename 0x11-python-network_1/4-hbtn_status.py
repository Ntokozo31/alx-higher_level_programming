#!/usr/bin/python3

"""
Our script will fatch URL with request package
"""

import requests

if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    t = r.text
    print("Body response: \n\t - type: {}\n\t - content: {}".format(type(t), t))
