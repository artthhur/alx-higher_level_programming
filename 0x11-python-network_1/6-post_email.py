#!/usr/bin/python3
"""
Module to send a POST request to a URL with an email parameter
and display the response body.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    responce = requests.post(url, data=value)
    print(responce.text)
