#!/usr/bin/python3

import sys

if __name__ == "__main__":
    arg_num = len(sys.argv) - 1
    if arg_num == 0:
        print("0 arguments.")
    elif arg_num == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_num))
    for i in range(arg_num):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
