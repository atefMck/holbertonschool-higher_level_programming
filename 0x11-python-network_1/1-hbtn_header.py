#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
from urllib import request
from sys import argv

url = argv[1]
with request.urlopen(url) as res:
    print(res.headers['X-Request-Id'])
