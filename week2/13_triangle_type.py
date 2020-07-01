'''
Даны три стороны треугольника a,b,c.
Определите тип треугольника с заданными сторонами.
Выведите одно из четырех слов: rectangular для прямоугольного треугольника,
acute для остроугольного треугольника,
obtuse для тупоугольного треугольника или
impossible, если треугольника с такими сторонами не существует
(считаем, что вырожденный треугольник тоже невозможен).
'''
a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    m = a
    p = b
    q = c
elif b >= a and b >= c:
    m = b
    p = a
    q = c
else:
    m = c
    p = a
    q = b
if m >= p + q:
    print('impossible')
elif m**2 == p**2 + q**2:
    print('rectangular')
elif m**2 > p**2 + q**2:
    print('obtuse')
elif m**2 < p**2 + q**2:
    print('acute')
else:
    print('impossible')
