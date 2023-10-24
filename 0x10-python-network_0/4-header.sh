#!/bin/bash
# Sends a GET request to an URL with a header variable.
curl -sH "X-School-User-Id: 98" "$1"
