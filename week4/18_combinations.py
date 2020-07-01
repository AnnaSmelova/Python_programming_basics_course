# По данным целым числам n и k (0≤k≤n) вычислите C из n по k.
# Решение оформите в виде функции C(n, k).
# Для решения используйте рекуррентное соотношение:
# И равенства:
# С(n, 1)=n
# C(n, n)=1


def binc(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    elif k == n:
        return 1
    else:
        return binc(n - 1, k) + binc(n - 1, k - 1)


x, y = int(input()), int(input())
print(binc(x, y))
