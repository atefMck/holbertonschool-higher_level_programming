#!/usr/bin/python3
""" Python script """
from sys import argv
from urllib import request, parse


def execute():
    """ Intermediate method for checker. """
    data = parse.urlencode({"email": argv[2]})
    data = data.encode('ascii')
    with request.urlopen(argv[1], data) as res:
        req = res.read()
        print(req.decode('utf-8'))


if __name__ == "__main__":
    execute()
