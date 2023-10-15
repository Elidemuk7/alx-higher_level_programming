#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """printsa a dictionary by ordered keys"""

    sorted_key = sorted(a_dictionary)

    for key in sorted_key:
        value = a_dictionary[key]

        print("{}: {}".format(key, value))
