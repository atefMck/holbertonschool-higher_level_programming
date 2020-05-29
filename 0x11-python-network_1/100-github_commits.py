#!/usr/bin/python3
""" Python script """
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def execute():
    """ Intermediate method for checker. """
    repo = argv[1]
    owner = argv[2]
    link = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    commits = requests.get(link).json()
    for commit in commits[:10]:
        string = "{}: {}".format(
            commit['sha'], commit.get('commit')['author']['name'])
        print(string)


if __name__ == "__main__":
    execute()
