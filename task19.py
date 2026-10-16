n, m = map(int, input().split('x'))
k=int(input())
if k < n * m and (k % n == 0 or k % m == 0): #(всегда отделяется кол-во кварталов, кратное n или m)
    print("успешно")
else:
    print("неосуществимо")