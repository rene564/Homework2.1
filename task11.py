import turtle
xc = int(input("xc= "))
yc = int(input("yc= "))
r = int(input("r= "))
x = int(input("x= "))
y = int(input("y= "))

turtle.penup()
turtle.goto(xc, yc - r) #начинает на r выше начала координат, надо опустить
turtle.pendown()
turtle.circle(r)

turtle.penup()
turtle.goto(x, y)
turtle.dot(8, "red")

d2 = (x - xc) ** 2 + (y - yc) ** 2 #расстояние между точками

if d2 < r ** 2:
    print(f"Точка ({x}, {y}) внутри окружности")
elif d2 == r ** 2:
    print(f"Точка ({x}, {y}) на окружности")
else:
    print(f"Точка ({x}, {y}) за пределами окружности")

turtle.done()