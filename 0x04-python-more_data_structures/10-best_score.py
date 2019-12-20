#!/usr/bin/python3
def best_score(a_dictionary):
    r = None
    if a_dictionary is not None:
        c = -90000
        for keys in a_dictionary.keys():
            if a_dictionary[keys] > c:
                c = a_dictionary[keys]
                r = keys
        return(r)
    return(None)
