#!/usr/bin/python3
""" Python script """
import requests
from sys import argv


def execute():
    """ Intermediate method for checker. """
    req = requests.post(argv[1], data={'email': argv[2]})
    print(req.text)


if __name__ == "__main__":
    execute()
