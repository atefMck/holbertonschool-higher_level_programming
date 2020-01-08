#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    try:
        for items in range(x):
            print("{}".format(my_list[items]), end="")
            c += 1
    except (TypeError, IndexError):
        pass
    print()
    return c
