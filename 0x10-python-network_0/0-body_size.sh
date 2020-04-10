#!/bin/bash
# Get conents length of URL
a=$(curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2)
echo ${a::-1} 