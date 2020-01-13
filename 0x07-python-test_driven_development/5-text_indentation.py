#!/usr/bin/python3
"""
File containing the text_indentation method.
text is the text to be treated
"""

def text_indentation(text):
    """ 'text_indentation(text)' print text in a weird way
        text is the text to be treated """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    cond = ['.', ',', '?', ':']
    char = 0
    while char < len(text):
        print("{}".format(text[char]), end="")
        if text[char] in cond:
            print()
            print()
            char += 1
        char += 1
    print()
