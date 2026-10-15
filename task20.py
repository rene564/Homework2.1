a,b = input()
b=int(b)

x1 = a=='a' or a=='c' or a=='e' or a=='g' #столбец нечет
x2 = b % 2 == 1 #строка нечет

if x1==x2:
    print("чёрный")
else:
    print("белый")