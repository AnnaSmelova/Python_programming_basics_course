# Для быстрого вычисления наибольшего общего делителя
# двух чисел используют алгоритм Евклида.
# Он построен на следующем соотношении: НОД(a,b)=НОД(b,a % b).
# Реализуйте рекурсивный алгоритм Евклида в виде функции gcd(a, b)


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    elif a > b:
        d = gcd(b, a % b)
    else:
        d = gcd(a, b % a)
    return d


x, y = int(input()), int(input())
print(gcd(x, y))
