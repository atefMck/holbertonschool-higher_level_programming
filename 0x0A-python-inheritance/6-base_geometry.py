#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        if hasattr(self, 'area'):
            raise Exception("area() is not implemented")
