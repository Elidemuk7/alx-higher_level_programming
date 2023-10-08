#!/usr/bin/python3
def uppercase(str):
    """converting to uppercase"""
    for i in str:
        if orc(i) >= 97 and orc(i) <= 122:
            char = chr(orc(i) - 32)
        print("{}".format(char), end= "")
    print("")
