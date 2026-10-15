n = int(input())
g = n // (17*29)
rest = n % (17*29)
si = rest // 29 #29 кнатов в одном сикле
kn = rest % 29 #остаток-это кнаты

if g > 0:
    print(f"{g} галлеонов")
if si > 0:
    print(f"{si} сиклей")
if kn > 0:
    print(f"{kn} кнатов")