#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    a funtion that replaces an element in a list
    """
    updated_list = list(my_list)
    for i in range(len(updated_list)):
        if idx < 0:
            return NONE
        elif idx > len(updated_list) - 1:
            return NONE
        else:
            updated_list[idx] = element
            return (updated_list)
