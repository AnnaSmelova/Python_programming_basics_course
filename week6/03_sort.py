# Отсортируйте данный массив, используя встроенную сортировку.

n = int(input())
l = list(map(int, input().split()))
l.sort()
print(*l)
