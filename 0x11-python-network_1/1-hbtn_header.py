#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
import urllib.request
import sys

with urllib.request.urlopen('https://intranet.hbtn.io') as req:
    print(req.headers['X-Request-Id'])
