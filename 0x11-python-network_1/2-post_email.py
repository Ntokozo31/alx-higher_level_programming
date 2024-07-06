#!/usr/bin/python3

# We are going to write a scrip that will take url and email
# We are going to check if the script is run dicectly

from urllib import request, parse
import sys

if __name__ == "__main__":

    # Assign our argumens
    my_values = {'email': sys.argv[2]}
    data = parse.urlencode(my_values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)

    # We open our url with our parameter
    with request.urlopen(req) as response:
        my_body = response.read()
        # We print out
        print(my_body.decode('utf-8'))
