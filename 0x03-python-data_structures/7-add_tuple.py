#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    copy_a = tuple_a
    copy_b = tuple_b
    if copy_a[0] == False:
        copy_a[0] = 0
    elif copy_a[1] == False:
        copy_a[1] = 0
    elif copy_b[0] == False:
        copy_b[0] = 0
    elif copy_b[1] == False:
        copy_b[1] = 0
    print(copy_a[0] + copy_b[0], copy_a[1] + copy_b[1])
