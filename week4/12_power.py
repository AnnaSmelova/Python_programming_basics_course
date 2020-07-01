# Дано действительное положительное число a и целоe число n.
# Вычислите aⁿ. Решение оформите в виде функции power(a, n).
# Стандартной функцией возведения в степерь пользоваться нельзя.


def power2(a, n):
    if n == 0:
        return 1
    elif n > 0:
        if n != 1:
            a *= power(a, n - 1)
    else:
        a = 1 / power(a, -n)
    return a


def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        r = a
        while n != 1:
            a *= r
            n -= 1
        return a
    else:
        r = a
        k = -n
        while k != 1:
            a *= r
            k -= 1
        return 1 / a


x, y = float(input()), int(input())
print(power(x, y))
