n, k, m = map(int, input().split())

a=2*n/k
if a>(2*n//k):
    sessions=2*n//k+1
else:
    sessions=2*n//k #округляем вверх кол-во сеансов, чтобы не было малышей которые не покатались

if sessions < 2: #если карусель вмещает больше детей, чем пришло
    sessions = 2

print(sessions * m)

