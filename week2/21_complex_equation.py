'''
Решить в целых числах уравнение: (ax+b) / (cx+d) =0
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a != 0:
    x = (-1 * b) // a
else:
    x = 'INF'
if c != 0:
    y = (-1 * d) // c
else:
    y = 'INF'
if a == 0 and b == 0 and c != 0:
    print('INF')
elif a == 0 and b != 0 or c == 0 and d == 0:
    print('NO')
elif (-1 * b) % a == 0 and x != y:
    print(x)
else:
    print('NO')
