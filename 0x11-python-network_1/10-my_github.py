#!/usr/bin/python3
"""
Module to fetch and display your GitHub user id using the access credentials
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth_cred = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth_cred)
    print(response.json().get("id"))
