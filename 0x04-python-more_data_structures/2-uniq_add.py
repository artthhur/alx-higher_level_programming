#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_integers = set()
    for element in my_list:
        if isinstance(element, int):
            unique_integers.add(element)
    total_sum = sum(unique_integers)
    return total_sum
