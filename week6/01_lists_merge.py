# Даны два целочисленных списка A и B, упорядоченных по неубыванию.
# Объедините их в один упорядоченный список С
# (то есть он должен содержать len(A)+len(B) элементов).
# Решение оформите в виде функции merge(A, B),
# возвращающей новый список.
# Алгоритм должен иметь сложность O(len(A)+len(B)).
# Модифицировать исходные списки запрещается.
# Использовать функцию sorted и метод sort запрещается.


def merge(a, b):
    c = []
    i, j = 0, 0
    for k in range(len(a) + len(b)):
        if i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        elif i < len(a):
            c.append(a[i])
            i += 1
        elif j < len(b):
            c.append(b[j])
            j += 1
    return c


l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(*merge(l1, l2))
