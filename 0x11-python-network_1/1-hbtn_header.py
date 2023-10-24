#!/usr/bin/python3
"""sends a request to a URL and displays the value of X-Request-Id variable."""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)

    with urllib.request.urlopen(request) as response:
        x_request_id = response.getheader('X-Request-Id')

        print(x_request_id)
