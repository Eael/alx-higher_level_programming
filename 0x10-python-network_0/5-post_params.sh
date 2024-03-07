#!/bin/bash
# Takes a URL and send a POST requests with variables
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
