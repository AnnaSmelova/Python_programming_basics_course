# Дан список чисел. Выведите все элементы списка,
# которые больше предыдущего элемента.

A = list(map(int, input().split()))
last = A[0]
for el in A:
    if el > last:
        print(el, end=' ')
    last = el
