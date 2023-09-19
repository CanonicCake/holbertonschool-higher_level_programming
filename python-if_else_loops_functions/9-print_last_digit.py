#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lastn = number % 10
    elif number < 0:
        lastn = (((number * -1) % 10) * -1)
    return lastn
