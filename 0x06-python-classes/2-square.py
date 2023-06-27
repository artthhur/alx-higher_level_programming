#!/usr/bin/python3

"""
This module defines the Square class.
"""


class Square:
    """
    Represents a square.
    """
    def __init__(self, size=0):
        """
        Initializes a square with the given size.

        Args:
            size (int): The size of the square (optional, default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
