# Даны два натуральных числа n и m.
# Сократите дробь (n / m), то есть выведите два других числа
# p и q таких, что (n / m) = (p / q) и дробь (p / q) — несократимая.
# Решение оформите в виде функции ReduceFraction(n, m),
# получающая значения n и m и возвращающей кортеж из двух чисел: return p, q.
# Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).


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


def ReduceFraction(n, m):
    d = gcd(n, m)
    p = n // d
    q = m // d
    return p, q


x, y = int(input()), int(input())
print(*ReduceFraction(x, y))
