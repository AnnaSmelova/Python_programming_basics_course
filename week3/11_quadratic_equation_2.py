'''
Даны произвольные действительные коэффициенты a, b, c.
Решите уравнение ax²+bx+c=0.
'''
import math

a, b, c = float(input()), float(input()), float(input())
D = b * b - 4 * a * c
if a == 0:
    if b == 0:
        if c == 0:
            print('3')
        else:
            print('0')
    else:
        print(1, -c / b)
else:
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        if x1 > x2:
            print(2, x2, x1)
        else:
            print(2, x1, x2)
    elif D == 0:
        x = -b / (2 * a)
        print(1, x)
    else:
        print('0')
