#!/usr/bin/python3
lower = __import__('7-islower').islower

print("a is {}".format("low" if lower("a") else "high"))
print("A is {}".format("low" if lower("A") else "high"))
