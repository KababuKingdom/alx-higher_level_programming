#!/usr/bin/python3
def simple_delete(my_dictionary, key=""):
    if my_dictionary:
        try:
            del my_dictionary[key]
        except KeyError:
            pass
    return my_dictionary
