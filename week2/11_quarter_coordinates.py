'''
Даны координаты двух точек на плоскости, требуется определить,
лежат ли они в одной координатной четверти или нет (все координаты отличны от нуля).
'''
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 > 0 and x2 > 0 or x1 < 0 and x2 < 0:
    if y1 > 0 and y2 > 0 or y1 < 0 and y2 < 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
