#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argv = sys.argv
len = len(argv)
print("{:d} arguments.".format(len - 1))
if len > 1:
    for i in range(1, len):
        print("{:d}: {:s}".format(i, argv[i]))
