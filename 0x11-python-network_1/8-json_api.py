#!/usr/bin/python3
"""
Module to send a POST request with a letter parameter and process the response
"""
import sys
import requests


if __name__ == "__main__":
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {"q": q}

    url = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        response = url.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
