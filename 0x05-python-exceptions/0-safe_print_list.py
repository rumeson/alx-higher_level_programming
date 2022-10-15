#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ele_printed = 0
    try:
        while ele_printed < x:
            print("{}".format(my_list[ele_printed]), end="")
            ele_printed += 1
        print()
        return ele_printed
    except IndexError:
        print("")
        return ele_printed
