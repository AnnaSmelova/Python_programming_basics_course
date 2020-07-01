# Выведите все четные элементы списка.

A = list(map(int, input().split()))
for el in A:
    if el % 2 == 0:
        print(el, end=' ')
