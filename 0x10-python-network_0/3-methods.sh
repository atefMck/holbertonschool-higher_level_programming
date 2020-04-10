#!/bin/bash
# Get conents length of URL
curl -sI "$1" | grep "Allow:" | cut -d " " -f 2-
