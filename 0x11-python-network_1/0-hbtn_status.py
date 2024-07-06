#!/usr/bin/python3

"""
We are going to write a script that will facth a URL
"""

import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        my_body = response.read()
        print("Body response")
        print("\t - type: {}".format(type(my_body)))
        print("\t - content: {}".format(my_body))
        print("\t - utf-8 content: {}".format(my_body.decode("utf-8")))
