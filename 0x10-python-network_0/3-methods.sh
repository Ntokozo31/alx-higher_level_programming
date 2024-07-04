#!/bin/bash
#Display all the HTTP methods the server will accept
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-
