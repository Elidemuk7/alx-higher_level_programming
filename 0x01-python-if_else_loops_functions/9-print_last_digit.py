#!/usr/bin/python3
def print_last_digit(number):
    for i in number:
        num = chr(int(number))
        print("{}".format(number[-1]), end="")
