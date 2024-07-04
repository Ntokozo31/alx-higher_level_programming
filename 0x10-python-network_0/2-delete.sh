#!/bin/bash
#Send delet requast to URL, display the body of the response
curl -s -X DELETE "${1}"
