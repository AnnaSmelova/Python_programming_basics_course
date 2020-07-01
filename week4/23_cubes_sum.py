# Напишите программу, которая представляет переданное
# натуральное число в виде суммы не более чем
# 7 кубов других натуральных чисел.


def cubes(n, r):
    k = int(n**(1/3.0))
    if k**3 == n:
        print(k**3, end='')
        return k**3
    while k >= 1:
        s = k**3
        if r + 1 <= 7:
            s += cubes(n - k**3, r + 1)
        if s == n:
            print(' ', k**3, sep='', end='')
            return int(s)
        k -= 1
    return 0


x = int(input())
res = cubes(x, 1)
if res == 0:
    print(0)
