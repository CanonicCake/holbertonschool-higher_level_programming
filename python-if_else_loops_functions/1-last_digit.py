#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastn = int(repr(number)[-1])
if lastn > 5:
    print(f"Last digit of {number} is {lastn} and is greater than 5")
elif lastn == 0:
    print(f"Last digit of {number} is {lastn} and is 0")
else:
    print(f"Last digit of {number} is {lastn} and is less than 6 and not 0")
