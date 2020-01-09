#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=()):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
        if position:
            error = "position must be a tuple of 2 positive integers"
            if len(position) != 2:
                raise TypeError(error)
            if not isinstance(position[0], int) or position[0] < 0:
                raise TypeError(error)
            if not isinstance(position[1], int) or position[1] < 0:
                raise TypeError(error)
            self.__position = position

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if hasattr(self, 'position'):
                for k in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                if hasattr(self, 'position'):
                    for l in range(self.__position[0]):
                        print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        return (self.__position)

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        error = "position must be a tuple of 2 positive integers"
        if len(value) != 2:
            raise TypeError(error)
        if not isinstance(value[0], int) or value[0] < 0:
            raise TypeError(error)
        if not isinstance(value[1], int) or value[1] < 0:
            raise TypeError(error)
        self.__position = value

    def __str__(self):
        print = ""
        if self.__size == 0:
            print += "\n"
        else:
            if hasattr(self, 'position'):
                for k in range(self.__position[1]):
                    print += "\n"
            for i in range(self.__size):
                if hasattr(self, 'position'):
                    for l in range(self.__position[0]):
                        if l != self.__position[0] - 1:
                            print += " "
                for j in range(self.__size):
                    print += "#"
                if i != self.__size - 1:
                    print += "\n"
        return (print)


my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)
