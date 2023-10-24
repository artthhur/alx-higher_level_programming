#!/bin/bash
# Gets the byte size of the HTTP response header for an URL
curl -s "$1" | wc -c
