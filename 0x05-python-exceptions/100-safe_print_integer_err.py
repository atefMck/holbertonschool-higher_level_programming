#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as error:
        sys.exit("Exception: {}".format(error.args[0]))
        return (False)
