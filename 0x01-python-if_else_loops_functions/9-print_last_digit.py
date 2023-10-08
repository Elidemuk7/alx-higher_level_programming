#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    last_dig = number % 10
    print(last_dig, end="")
    return (last_dig)
