#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
import urllib.request
from sys import argv

with urllib.request.urlopen(argv[1]) as req:
    print(req.headers['X-Request-Id'])
