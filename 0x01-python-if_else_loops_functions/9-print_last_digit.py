#!/usr/bin/python3
def print_last_digit(number):
    last_digi = abs(number) % 10

    print("{}".format(last_digi), end="")
    return last_digi
