#!/usr/bin/python3
def remove_char_at(str, n):
    copy_str = ""
    for i in str:
        if n > (len(str) - 1) or n < 0:
            return str
        elif i != str[n]:
            copy_str += i
    return copy_str
