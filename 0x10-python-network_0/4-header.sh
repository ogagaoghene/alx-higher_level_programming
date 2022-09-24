#!/bin/bash
# Send a GET request to a given URL with a header variable.
curl -sH "X-School-User-Id: 98" 0.0.0.0:5000/catch_me "${1}"
