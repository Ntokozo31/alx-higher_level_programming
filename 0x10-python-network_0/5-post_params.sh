#!/bin/bash
#Send a post requast to past URL, display the body of the response
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "${1}" 
