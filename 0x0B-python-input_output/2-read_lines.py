#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r', encoding="utf-8") as file:
        if nb_lines <= 0:
            print(file.read(), end="")
        else:
            for i in range(nb_lines):
                print(file.readline(), end="")
