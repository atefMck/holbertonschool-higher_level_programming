#!/usr/bin/python3
""" Python script """
import requests
from sys import argv


def execute():
    """ Intermediate method for checker. """
    req = requests.get(argv[1])
    stat = req.status_code
    if stat >= 400:
        print("Error code:", req.status_code)
    else:
        print(req.text)


if __name__ == "__main__":
    execute()
