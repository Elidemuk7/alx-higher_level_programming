#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    A function that prints the elements of a list
    """
    for i in range(len(my_list)):
        if i >= 0:
            print("{:d}".format(my_list[i]))
