#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        s = fct(*args)
        return (s)
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error.args[0]))
        return (None)
