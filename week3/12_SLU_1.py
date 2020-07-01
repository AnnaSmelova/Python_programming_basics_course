'''
Даны вещественные числа a, b, c, d, e, f.
Известно, что система линейных уравнений:

ax + by = e

cx + dy = f

имеет ровно одно решение.
Выведите два числа x и y, являющиеся решением этой системы.
'''
a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
if a == 0 and d == 0:
    x = f / c
    y = e / b
elif b == 0 and c == 0:
    x = e / a
    y = f / d
else:
    y = (a * f - c * e) / (a * d - b * c)
    x = (e - b * y) / a
print(x, y)
