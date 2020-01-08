#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_r = []
    r = 0
    for i in range(list_length):
        try:
            r = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            r = 0
        except IndexError:
            print("out of range")
            r = 0
        except TypeError:
            print("wrong type")
            r = 0
        finally:
            my_list_r.insert(i, r)
    return (my_list_r)
