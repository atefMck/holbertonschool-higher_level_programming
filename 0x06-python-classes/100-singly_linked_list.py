#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer")
        if isinstance(next_node, Node) or next_node is None:
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    def area(self):
        return (self.__size ** 2)

    @property
    def data(self):
        return (self.__data)

    @property
    def next_node(self):
        return (self.__next_node)

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        current = self.__head
        if self.__head is None or value < self.__head.data:
            self.__head = Node(value, self.__head)
        else:
            while current.next_node is not None:
                if current.next_node.data > value:
                    break
                current = current.next_node
            current.next_node = Node(value, current.next_node)

    def __str__(self):
        print = ""
        current = self.__head
        if current is None:
            return print
        while current is not None:
            print += str(current.data)
            current = current.next_node
            if current is not None:
                print += "\n"
        return print
