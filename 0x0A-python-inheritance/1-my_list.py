#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        newList = eval(repr(self))
        newList.sort()
        print(newList)
