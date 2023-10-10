#!/usr/bin/python3

def element_at(my_list, idx):
    """
    a funtion that retrieves an element from a list
    """
    for i in range(len(my_list)):
        if idx < 0:
            return NONE
        elif idx > len(my_list) - 1:
            return NONE
        else:
            return (my_list[idx])
