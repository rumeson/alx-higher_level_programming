def safe_print_list(my_list=[], x=0):
    ele_printed = 0
    while ele_printed < x:
        try:    
            print("{}".format(my_list[ele_printed]), end="")
            ele_printed += 1
        except IndexError:
            break
    print()
    return ele_printed
