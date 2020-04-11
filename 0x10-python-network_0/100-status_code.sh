#!/bin/bash
# Get conents length of URL
curl -s -o /dev/null -w "%{http_code}" "$1"
