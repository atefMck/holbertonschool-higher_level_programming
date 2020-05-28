#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
from urllib import request
from sys import argv

with request.urlopen(argv[1]) as req:
    print(req.headers['X-Request-Id'])
