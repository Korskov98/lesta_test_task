class Quad():
    
    def __init__(self, x, y, side1, side2, color):
        self.__x = x
        self.__y = y
        self.__side1 = side1
        self.__side2 = side2
        self.__color = color
        
    def draw(self):
        print("Drawing Quad: (" + str(self.__x) + ", " + str(self.__y) + ") with sides: " + str(self.__side1) + ", " + str(self.__side2) + ". Color:" + str(self.__color))