#!/usr/bin/python3
""" find_peak function """


def find_peak(list_of_integers):
    start = 0
    length = len(list_of_integers)
    end = length - 1
    peak = None
    while start <= end:
        mid = (start + end) // 2
        peak = list_of_integers[mid]
        left = list_of_integers[mid - 1]
        right = list_of_integers[mid + 1]
        if (mid == 0 or peak >= left) and (mid == length - 1 or peak >= right):
            break
        elif mid < length - 1 and peak < right:
            start = mid + 1
        else:
            end = mid - 1
    return peak
