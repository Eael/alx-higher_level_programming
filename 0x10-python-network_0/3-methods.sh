#!/bin/bash
# Takes a URL and display HTTP requests it accepts
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
