#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        c = my_list[0]
        for element in my_list:
            if c < element:
                c = element
    else:
        return(None)
    return(c)
