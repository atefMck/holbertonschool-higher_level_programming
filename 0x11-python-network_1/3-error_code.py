#!/usr/bin/python3
""" Python script """
from sys import argv
from urllib import request, error


def execute():
    """ Intermediate method for checker. """
    try:
        with request.urlopen(argv[1]) as res:
            req = res.read()
            print(req.decode('utf-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)


if __name__ == "__main__":
    execute()
