a, b = map(int, input().split('x'))
c, d, e = map(int, input().split('x'))
#p-наименьшая, q-наибольшая сторона отверстия
if a < b:
    p = a
    q = b
else:
    p = b
    q = a

if c <= d and c <= e:
    x = c
    if d < e: y = d
    else: y = e
elif d <= c and d <= e:
    x = d
    if c < e: y = c
    else: y = e
else:
    x = e
    if c < d:
        y = c
    else:
        y = d
#наименьшая грань кирпича должна пролезть в отверстие
if x <= p and y <= q:
    print("да")
else:
    print("нет")