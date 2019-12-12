#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
argv = sys.argv
len = len(argv)

if len != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
a = int(argv[1])
b = int(argv[3])
op = argv[2]
if op != "+" and op != "-" and op != "*" and op != "/":
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
if op == "+":
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, add(a, b)))
if op == "-":
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, sub(a, b)))
if op == "*":
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, mul(a, b)))
if op == "/":
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, div(a, b)))
