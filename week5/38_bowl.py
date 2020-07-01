# N кеглей выставили в один ряд, занумеровав их слева
# направо числами от 1 до N.
# Затем по этому ряду бросили K шаров, при этом i-й шар
# сбил все кегли с номерами от lᵢ до rᵢ включительно.
# Определите, какие кегли остались стоять на месте.

n, k = list(map(int, input().split()))
b = []
for _ in range(k):
    l, r = list(map(int, input().split()))
    b.append([l, r])

a = []
for _ in range(n):
    a.append('I')

for el in b:
    for i in range(el[0] - 1, el[1]):
        a[i] = '.'

for g in a:
    print(g, end='')
