#!/usr/bin/python3
def no_c(my_string):
    copy = [elmt for elmt in my_string if elmt != 'c' and elmt != 'C']
    return "".join(copy)
