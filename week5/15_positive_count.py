# Найдите количество положительных элементов в данном списке.

A = list(map(int, input().split()))
s = 0
for el in A:
    if el > 0:
        s += 1
print(s)
