#!/bin/bash
# Get conents length of URL
curl -sI "$1" | grep "Content-Length" | cut -d " " -f 2