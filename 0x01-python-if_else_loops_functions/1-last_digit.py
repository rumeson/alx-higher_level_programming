#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
last_num = math.fmod(number, 10)
print("Last digit of {} is {} and is".format(number, last_num), end=" ")
if last_num > 5:
    print("greater than 5")
elif last_num == 0:
    print(0)
elif last_num < 6 and last_num != 0:
    print("less than 6 and not 0")
