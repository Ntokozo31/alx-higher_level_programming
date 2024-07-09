#!/usr/bin/python3

"""We are going to send a request to URL and displays the body of the response"""


if __name__ == '__main__':
    from requests import post
    from sys import argv
    URL = "http://0.0.0.0:5000/search_user"

    data = {'q': argv[1] if len(argv) >= 2 else ""}
    response = post(URL, data)
    type_respo = response.headers['content-type']

    if type_respo == 'application/json':
        results = response.json()
        _id = results.get('id')
        name = results.get('name')
        if (results != {} and _id and name):
            print("[{}] {}".format(_id, name))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
