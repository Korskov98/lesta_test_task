class Circle():
    
    def __init__(self, radius, x, y, color):
        self.__radius = radius
        self.__x = x
        self.__y = y
        self.__color = color      
        
    def draw(self):
        print("Drawing Circle: (" + str(self.__x) + ", " + str(self.__y) + ") with radius " + str(self.__radius) + ". Color:" + str(self.__color))