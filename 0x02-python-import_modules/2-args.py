#!/usr/bin/python3

"""
a python script that prints the list of args
"""

if __name__ == "__main__":

    import sys

    nums_args = len(sys.argv) -1
    if nums_args == 0:
        print("0 argument.")
    elif nums_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(nums_args))

    for i in range(nums_args):
        print("{}: {}".format(i+1, sys.argv[i+1]))
