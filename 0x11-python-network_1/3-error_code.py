#!/usr/bin/python3
""" This is a script that
- takes in a URL
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
- manage urllib.error.HTTPError exceptions and print:
    Error code: followed by the HTTP status code
"""

from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as e:
        print("Error Code: {}".format(e.code))
