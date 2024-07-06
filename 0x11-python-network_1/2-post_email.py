#!/usr/bin/python3

"""
We are going to write a scrip that will take url and email
sends a post request to the passed URL with the email as parameter
and displays the body of the response decoded in utf-8
"""

from urllib import request, parse
import sys

if __name__ == "__main__":

    my_values = {'email': sys.argv[2]}
    data = parse.urlencode(my_values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)

    with request.urlopen(req) as response:
        my_body = response.read()
        print(my_body.decode('utf-8'))
