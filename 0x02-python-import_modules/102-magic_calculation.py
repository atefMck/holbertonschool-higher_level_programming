#!/usr/bin/python3
if __name__ == '__main__':
    from magic_calculation_102 import add
    from magic_calculation_102 import sub
if a < b:
    c = add(a, b)
    for i in range(4, 6):
        c = c + i
    return(c)
else:
    return(sub(a, b))
