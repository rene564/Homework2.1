n = int(input())
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
a1 = 1000<=n <= 9999
a2 = a != b and a != c and a != d and b != c and b != d and c != d
a3 = not(1900<=n<=2050)
if a1 and a2 and a3: print("OK")
else: print("ERROR")