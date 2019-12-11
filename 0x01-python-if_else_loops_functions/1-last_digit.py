#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number < 0:
    ld = (-number) % 10
    if ld == 0:
        print("Last digit of {:d} is {:d}".format(number, ld))
    else:
        print("Last digit of {:d} is -{:d}".format(number, ld))
elif number > 0:
    ld = number % 10
    print("Last digit of {:d} is {:d}".format(number, ld))
else:
    print("Last digit of 0 is 0")
