#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all integers in a list"""
    unique_set = set()
    total = 0

    for num in my_list:
        if num not in unique_set:
            total += num
            unique_set.add(num)

    return total
