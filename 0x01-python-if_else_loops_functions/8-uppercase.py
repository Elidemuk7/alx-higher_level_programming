#!/usr/bin/python3
def uppercase(str):
    """converting to uppercase"""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            char = chr(ord(i) - 32)
        elif ord(i) >= 32 and ord(i) <= 96:
            char = chr(ord(i))
        elif ord(i) >= 123 and ord(i) <= 126:
            char = chr(ord(i))
        print("{}".format(char), end="")
    print("")
