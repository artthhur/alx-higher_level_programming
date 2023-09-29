#!/usr/bin/python3
"""
Module to send request to a URL and display the value of X-Request-Id variable
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    x_request_id = requests.get(url)
    print(x_request_id.headers.get("X-Request-Id"))
