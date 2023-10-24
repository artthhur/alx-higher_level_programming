#!/bin/bash
# sends a POST request to an URL.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
