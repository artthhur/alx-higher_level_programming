#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiplesList = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiplesList.append(True)
        else:
            multiplesList.append(False)

    return multiplesList
