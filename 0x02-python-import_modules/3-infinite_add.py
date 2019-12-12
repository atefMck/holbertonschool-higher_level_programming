#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argv = sys.argv
len = len(argv)
sum = 0
if len > 1:
    for i in range(1, len):
        sum += int(argv[i])
print("{:d}".format(sum))
