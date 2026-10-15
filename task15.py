n, k, m = map(int, input().split())
if k > m: d = k - m
else: d = m - k
steps = d
if n - d < steps:
    print(n-d-1)
else:
    print(steps - 1)