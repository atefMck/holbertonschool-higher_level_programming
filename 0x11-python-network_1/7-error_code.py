#!/usr/bin/python3
""" Python script """
import requests
from sys import argv


def execute():
    """ Intermediate method for checker. """
    req = requests.get(argv[1])
    print(req.status_code)


if __name__ == "__main__":
    execute()
