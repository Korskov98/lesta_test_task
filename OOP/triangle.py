class Triangle():
    
    def __init__(self, x1, y1, x2, y2, x3, y3, color):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__x3 = x3
        self.__y3 = y3
        self.__color = color       
        
    def draw(self):
        print("Drawing Tringle: (" + str(self.__x1) + ", " + str(self.__y1) + "), " + "(" + str(self.__x2) + ", " + str(self.__y2) + "), " + "(" + str(self.__x3) + ", " + str(self.__y3) + ")" + ". Color:" + str(self.__color))