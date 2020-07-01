import math

# Проверьте, принадлежит ли точка данной закрашенной области
# Если точка принадлежит области (область включает границы),
# выведите слово YES, иначе выведите слово NO.
# Решение должно содержать функцию IsPointInArea(x, y),
# возвращающую True, если точка принадлежит области и False,
# если не принадлежит.
# Основная программа должна считать координаты точки,
# вызвать функцию IsPointInArea и в зависимости от возвращенного
# значения вывести на экран необходимое сообщение.
# Функция IsPointInArea не должна содержать инструкцию if.


def sgm_lng(a, b, c, d):
    return math.sqrt((c - a)**2 + (d - b)**2)


def IsPointInCircle(a, b, ac, bc, rad):
    return sgm_lng(a, b, ac, bc) < rad


def IsPointOnCircle(a, b, ac, bc, rad):
    return sgm_lng(a, b, ac, bc) == rad


def IsPointInArea(x, y):
    x = round(x, 5)
    y = round(y, 5)
    c0 = IsPointOnCircle(x, y, -1, 1, 2)
    c1 = IsPointInCircle(x, y, -1, 1, 2)
    c2 = y >= -x and y >= 2 * x + 2
    c3 = y <= -x and y <= 2 * x + 2
    return (c1 or c0) and c2 or not c1 and c3


a, b = float(input()), float(input())
if IsPointInArea(a, b):
    print('YES')
else:
    print('NO')
