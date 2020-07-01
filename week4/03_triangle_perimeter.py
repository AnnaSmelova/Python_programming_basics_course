import math

# Напишите функцию, вычисляющую длину отрезка по координатам его концов.
# С помощью этой функции напишите программу,
# вычисляющую периметр треугольника по координатам трех его вершин.


def sgm_lng(a, b, c, d):
    return math.sqrt((c - a)**2 + (d - b)**2)


x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
x3, y3 = int(input()), int(input())
p = sgm_lng(x1, y1, x2, y2)
p += sgm_lng(x2, y2, x3, y3)
p += sgm_lng(x3, y3, x1, y1)
print(p)
