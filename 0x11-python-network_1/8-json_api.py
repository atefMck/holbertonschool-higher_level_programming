#!/usr/bin/python3
""" Python script """
import requests
from sys import argv


def execute():
    """ Intermediate method for checker. """
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    data = {"q": q}
    req = requests.post("http://0.0.0.0:5000/search_user", data)
    try:
        print("[{}] {}".format(req.json()['id'], req.json()['name']))
    except ValueError:
        print("Not a valid JSON")
    except:
        print("No result")


if __name__ == "__main__":
    execute()
