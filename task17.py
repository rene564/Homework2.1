a,b=map(int, input().split('x'))
r = 6.5
if a ** 2 + b ** 2 <= (2 * r) ** 2: #диагональ прям в кв не больше диаметра в кв
    print("да")
else: print("нет")