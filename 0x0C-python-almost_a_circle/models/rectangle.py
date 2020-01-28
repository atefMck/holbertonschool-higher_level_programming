#!/usr/bin/python3
"""Rectange Class."""
from models.base import Base


class Rectangle(Base):
    """New Rectange Class, inheriting from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init method for Rectangle class"""
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method returning area of rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """method displaying rectangle"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for l in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args):
        """method updating rectangle"""
        if len(args) == 1:
            self.id = args[0]
        if len(args) == 2:
            self.id = args[0]
            self.__width = args[1]
        if len(args) == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
        if len(args) == 4:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
        if len(args) == 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]

    def __str__(self):
        """method formatting string rectangle output"""
        string0 = "[Rectangle] ({}) ".format(self.id)
        string1 = "{}/{} ".format(self.__x, self.__y)
        string2 = "- {}/{}".format(self.__width, self.__height)
        return(string0 + string1 + string2)
