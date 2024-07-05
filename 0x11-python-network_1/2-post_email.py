#!/usr/bin/python3

# We are going to write a scrip that will take url and email
# We are going to check if the script is run dicectly

if __name__ == "__main__":
    # We import neccesary modules
    import urllib.request
    import urllib.parse
    import sys

    # Assign our argumens
    argv = sys.argv
    url = argv[1]
    email =argv[2]
    data = urllib.parse.urlencode({"email": email})
    data = data.encode('ascii')

    # We open our url with our parameter
    with urllib.request.urlopen(url, data) as response:
        # We print out
        print(response.read().decode("utf-8"))
