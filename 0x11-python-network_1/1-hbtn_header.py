#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
from sys import argv
from urllib import request


def run():
    """ Intermediate method for checker. """
    with request.urlopen(argv[1]) as res:
        print(res.headers['X-Request-Id'])


if __name__ == "__main__":
    run()
