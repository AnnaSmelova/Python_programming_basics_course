'''
Даны числа a, b, c, d, e, f.
Решите систему линейных уравнений

ax + by = e

cx + dy = f
'''
a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
delta = a * d - b * c
delta1 = e * d - b * f
delta2 = a * f - e * c
if delta != 0:
    x = delta1 / delta
    y = delta2 / delta
    print('2', x, y)
else:
    if delta1 != 0 and delta2 != 0:
        print(0)
    elif delta1 == 0 and delta2 == 0:
        if a == b == c == d == e == f == 0:
            print(5)
        elif a == 0 and c == 0:
            if b != 0:
                print(4, e / b)
            elif d != 0:
                print(4, f / d)
            else:
                print(0)
        elif b == 0 and d == 0:
            if a != 0:
                print('3', e / a)
            elif c != 0:
                print('3', f / c)
        elif c != 0 and d != 0 and a // c == b // d:
            print('1', -c / d, f / d)
        elif a != 0 and b != 0 and c // a == d // b:
            print('1', -a / b, e / b)

    elif delta1 == 0 and delta2 != 0:
        print(0)
    elif delta1 != 0 and delta2 == 0:
        print(0)
