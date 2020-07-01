'''
Даны действительные коэффициенты a, b, c, при этом a != 0.
Решите квадратное уравнение ax²+bx+c=0 и выведите все его корни.
'''
import math

a, b, c = float(input()), float(input()), float(input())
D = b * b - 4 * a * c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)
elif D == 0:
    x = -b / (2 * a)
    print(x)
