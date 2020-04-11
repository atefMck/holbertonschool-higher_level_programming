#!/bin/bash
# Get conents length of URL
curl -sL -X POST "$1" -H "Content-Type: application/json" -d @"$2"
