#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    result = True
    try:
        print("{:d}".format(value))
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        result = False
    return result
