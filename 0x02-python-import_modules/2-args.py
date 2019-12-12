#!/usr/bin/python3
import sys
argv = sys.argv
len = len(argv)
print("{:d} arguments.".format(len))
if len > 1:
    for i in range(1, len):
        print("{:d}: {:s}".format(i, argv[i]))
