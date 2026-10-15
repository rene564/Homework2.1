n = int(input())
a = n % 10
b = n % 100

if b >= 11 and b <= 14: print(n, "попугаев")
elif a == 1: print(n, "попугай")
elif a >= 2 and a <= 4: print(n, "попугая")
else: print(n, "попугаев")