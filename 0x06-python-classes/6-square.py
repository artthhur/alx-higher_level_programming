#!/usr/bin/python3

"""
This module defines the Square class.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with the given size and position.

        Args:
            size (int): The size of the square (optional, default is 0).
            position (tuple): The position of the square

        Raises:
            TypeError: If size is not an integer or position is not a tuple of
                       2 positive integers.
            ValueError: If size is < 0 or contains non-positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
            ValueError: If position contains non-positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(coord, int) for coord in value) or \
                not all(coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#'.

        If the size is 0, it prints an empty line.
        The position is used to add spaces before the square on each line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
