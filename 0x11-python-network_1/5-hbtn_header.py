#!/usr/bin/python3
""" Python script """
import requests
from sys import argv


def execute():
    """ Intermediate method for checker. """
    try:
        req = requests.get(argv[1])
        print(req.headers["X-Request-Id"])
    except requests.exceptions.ConnectionError as e:
        pass


if __name__ == "__main__":
    execute()
