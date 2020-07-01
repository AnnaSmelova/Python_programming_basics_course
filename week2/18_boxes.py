'''
Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂.
Определите, можно ли разместить одну из этих коробок внутри другой, при условии,
что поворачивать коробки можно только на 90 градусов вокруг ребер.
'''
A1, B1, C1 = int(input()), int(input()), int(input())
A2, B2, C2 = int(input()), int(input()), int(input())
if A1 >= B1 and A1 >= C1:
    a1 = A1
    if B1 >= C1:
        b1 = B1
        c1 = C1
    else:
        b1 = C1
        c1 = B1
elif B1 >= A1 and B1 >= C1:
    a1 = B1
    if A1 >= C1:
        b1 = A1
        c1 = C1
    else:
        b1 = C1
        c1 = A1
else:
    a1 = C1
    if B1 >= A1:
        b1 = B1
        c1 = A1
    else:
        b1 = A1
        c1 = B1
if A2 >= B2 and A2 >= C2:
    a2 = A2
    if B2 >= C2:
        b2 = B2
        c2 = C2
    else:
        b2 = C2
        c2 = B2
elif B2 >= A2 and B2 >= C2:
    a2 = B2
    if A2 >= C2:
        b2 = A2
        c2 = C2
    else:
        b2 = C2
        c2 = A2
else:
    a2 = C2
    if B2 >= A2:
        b2 = B2
        c2 = A2
    else:
        b2 = A2
        c2 = B2
if a1 == a2 and b1 == b2 and c1 == c2:
    print('Boxes are equal')
elif a1 >= a2 and b1 >= b2 and c1 >= c2:
    print('The first box is larger than the second one')
elif a1 <= a2 and b1 <= b2 and c1 <= c2:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')
