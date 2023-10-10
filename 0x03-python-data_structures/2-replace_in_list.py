#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    a funtion that replaces an element in a list
    """
    for i in range(len(my_list)):
        if idx < 0:
            return NONE
        elif idx > len(my_list) - 1:
            return NONE
        else:
            my_list[idx] = element
            return (my_list)
