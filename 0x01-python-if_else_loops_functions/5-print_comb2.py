#!/usr/bin/python3
for i in range(100):
    print("{:03}".format(i), end=', ' if i < 99 else '\n')
