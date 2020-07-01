# Дан список. Определите, является ли он монотонно возрастающим
# (то есть верно ли, что каждый элемент этого списка больше предыдущего).
# Выведите YES, если массив монотонно возрастает и NO в противном случае.
# Решение оформите в виде функции IsAscending(A).
# В данной функции должен быть один цикл while,
# не содержащий вложенных условий и циклов
# — используйте схему линейного поиска


def IsAscending(A):
    pr = ''
    for i in range(len(A)):
        if pr == '':
            pr = A[i]
        else:
            if A[i] <= pr:
                return False
            else:
                pr = A[i]
    return True

l = list(map(int, input().split()))
if IsAscending(l):
    print('YES')
else:
    print('NO')
