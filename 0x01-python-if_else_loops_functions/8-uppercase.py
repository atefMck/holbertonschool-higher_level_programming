#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) in range(97, 123):
            c = chr(ord(str[i]) - 32)
        else:
            c = str[i]
        print(c, end='')
    print()
