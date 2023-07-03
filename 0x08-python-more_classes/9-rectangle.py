#!/usr/bin/python3
"""Defines a Rectangle class module."""


class Rectangle:
    """
    Class that defines a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance
        Args:
            width (int): Width of the rectangle (default: 0)
            height (int): Height of the rectangle (default: 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle
        Returns:
            int: Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        Args:
            value (int): Width value to set
        Raises:
            TypeError: If the width is not an integer
            ValueError: If the width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle
        Returns:
            int: Height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        Args:
            value (int): Height value to set
        Raises:
            TypeError: If the height is not an integer
            ValueError: If the height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle
        Returns:
            int: Area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        Returns:
            int: Perimeter of the rectangle
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        Returns:
            str: String representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for i in range(self.__height):
            rect_str += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        that can be used to create a new instance using eval()
        Returns:
            str: String representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when the rectangle instance is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the one with the greater area
        Args:
            rect_1 (Rectangle): First rectangle
            rect_2 (Rectangle): Second rectangle
        Returns:
            Rectangle: The rectangle with the greater area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Creates a new Rectangle instance with equal width and height
        Args:
            size (int): Size of the square (default: 0)
        Returns:
            Rectangle: New rectangle instance representing a square
        """
        return cls(size, size)
