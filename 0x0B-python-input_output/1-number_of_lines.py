#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, 'r', encoding="utf-8") as file:
        count = len(file.readlines())
    return count

filename = "my_file_0.txt"
nb_lines = number_of_lines(filename)
print("{} has {:d} lines".format(filename, nb_lines))
