#!/usr/bin/python3
""" Python script """
import requests


def execute():
    """ Intermediate method for checker. """
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(req.text))
    print("\t- content:", req.text)


if __name__ == "__main__":
    execute()
