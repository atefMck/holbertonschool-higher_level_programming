#!/usr/bin/python3
""" Python script """
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def execute():
    """ Intermediate method for checker. """
    user = argv[1]
    pwd = argv[2]
    link = "https://api.github.com/users/{}".format(user)
    req = requests.get(link, auth=HTTPBasicAuth(user, pwd))
    print(req.json().get('id'))


if __name__ == "__main__":
    execute()
