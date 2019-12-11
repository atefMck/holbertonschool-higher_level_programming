#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) in range(97, 123):
            print("{:s}".format(chr(ord(str[i]) - 32)), end="")
        else:
            print(str[i], end='')
    print()
