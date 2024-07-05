#!/bin/bash
#Script that send request to a passed URL and display only the status odf the code
curl -so /dev/null -w "%{http_code}" "${1}"
