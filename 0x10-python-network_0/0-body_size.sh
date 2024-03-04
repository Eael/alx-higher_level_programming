#!/bin/bash
# GET response with size in bytes
curl -s "$1" | wc -c
