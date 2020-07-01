'''
Даны три целых числа A, B, C.
Определить, есть ли среди них хотя бы одно четное и хотя бы одно нечетное.
'''
A = int(input())
B = int(input())
C = int(input())
ch = A % 2 == 0 or B % 2 == 0 or C % 2 == 0
nch = A % 2 == 1 or B % 2 == 1 or C % 2 == 1
if ch and nch:
    print('YES')
else:
    print('NO')
