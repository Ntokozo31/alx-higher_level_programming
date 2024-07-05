#!/usr/bin/python3
# We are going to write a script that will facth a URL

import urllib.request

# We are chicking if the script is run directly or what
if __name__ == "__main__":
    # WE are going to creat a request object now
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    # Now it time to open our URL
    with urllib.request.urlopen(req) as response:
        # Now let us read our response
        my_body = response.read()
        # Let us first print the header
        print("Body response")
        # Let us print the type of our response body
        print("\t - type: {}".format(type(my_body)))
        # Let print the core content of response of the body
        print("\t - content: {}".format(my_body))
        # Let print UFT-8 decoded content of the response of our body
        print("\t - utf-8 content: {}".format(my_body.decode("utf-8")))
