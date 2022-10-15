def safe_print_list(my_list=[], x=0):
    ele_printed = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            ele_printed += 1
        except IndexError:
            break
    print()
    return ele_printed
