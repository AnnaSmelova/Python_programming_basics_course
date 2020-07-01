'''
Заданы две клетки шахматной доски.
Если они покрашены в один цвет, то выведите слово YES,
а если в разные цвета – то NO.
'''
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if a1 % 2 == b1 % 2 and a2 % 2 == b2 % 2:
    print('YES')
elif a1 % 2 != b1 % 2 and a2 % 2 != b2 % 2:
    print('YES')
else:
    print('NO')
