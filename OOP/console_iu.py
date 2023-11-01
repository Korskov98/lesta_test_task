from engine2d import Engine2D

engine = Engine2D();
while 1:
    command = str(input("Введите команду:"))
    if command == "c":
        radius = int(input("Введите радиус круга: "))
        x = int(input("Введите координату x точки: "))
        y = int(input("Введите координату y точки: "))
        engine.add_circle(radius, x, y)
    elif command == "t":
        x = int(input("Введите координату x первой точки: "))
        y = int(input("Введите координату y первой точки: "))
        x1 = int(input("Введите координату x второй точки: "))
        y1 = int(input("Введите координату y второй точки: "))
        x2 = int(input("Введите координату x третьей точки: "))
        y2 = int(input("Введите координату y третьей точки:: "))
        engine.add_triangle(x, y, x1, y1, x2, y2)
    elif command == "q":
        x = int(input("Введите координату x точки: "))
        y = int(input("Введите координату y точки: "))
        x1 = int(input("Введите длину первой стороны: "))
        y1 = int(input("Введите длину второй стороны: "))
        engine.add_quad(x, y, x1, y1)
    elif command == "d":
        engine.draw()
    elif command == "ch":
        color = int(input("Введите номер цвета: "))
        engine.change_color(color)
    elif command == "e":
        break
