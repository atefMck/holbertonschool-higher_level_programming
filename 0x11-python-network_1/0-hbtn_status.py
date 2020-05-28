#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as f:
    req = f.read()
    print('Body response:')
    print('\t- type:', type(req))
    print('\t- content:', req)
    print('\t- utf8 content:', req.decode('utf-8'))
