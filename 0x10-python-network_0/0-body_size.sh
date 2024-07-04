#!/bin/bash
#Send a request to that URL and display the size of the body of response
curl -s "${1}" | wc -c
