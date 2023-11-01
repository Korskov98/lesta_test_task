from typing import List
from circle import Circle
from triangle import Triangle
from quad import Quad

class Engine2D:

    def __init__(self):
        self.__canvas = []
        self.__color = 0
        
    def change_color(self, color):
        self.__color = color
        
    def get_color(self):
        return self.__color
        
    def get_canvas(self):
        return self.__canvas
        
    def add_triangle(self, x1, y1, x2, y2, x3, y3):
        triangle = Triangle(x1, y1, x2, y2, x3, y3, self.__color)
        self.__canvas.append(triangle)
        
    def add_circle(self, radius, x, y):
        circle = Circle(radius, x, y, self.__color)
        self.__canvas.append(circle)
    
    def add_quad(self, x, y, s1, s2):
        quad = Quad(x, y, s1, s2, self.__color)
        self.__canvas.append(quad)
        
    def draw(self):
        for val in self.__canvas:
            val.draw()
        self.__canvas.clear()