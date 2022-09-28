#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_num = str(number)
for num in str_num:
    if num == str_num[-1]:
        num = int(num)
        print("Last digit of {:d} is {:d} and is".format(number, num), end=" ")
        if num > 5:
            print("greater than 5")
        elif num == 0:
            print(0)
        elif num < 6 and num != 0:
            print("less than 6 and not 0")
