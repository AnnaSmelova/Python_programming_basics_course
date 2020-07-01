'''
Вдоль прямой выложены три спички.
Необходимо переложить одну из них так, чтобы при поджигании любой спички сгорали все три.
Для того чтобы огонь переходил с одной спички на другую,
необходимо чтобы эти спички соприкасались (хотя бы концами).

Требуется написать программу, определяющую, какую из трех спичек необходимо переместить.
'''
l1, r1 = int(input()), int(input())
l2, r2 = int(input()), int(input())
l3, r3 = int(input()), int(input())
# l1, r1, l2, r2, l3, r3 = 5, 6, 7, 8, 2, 4
s1 = r1 - l1
s2 = r2 - l2
s3 = r3 - l3
order = []  # num, left, right, length
if l1 <= l2 and l1 <= l3:
    order.append([1, l1, r1, s1])
    if l2 <= l3:
        order.append([2, l2, r2, s2])
        order.append([3, l3, r3, s3])
    else:
        order.append([3, l3, r3, s3])
        order.append([2, l2, r2, s2])
elif l2 <= l1 and l2 <= l3:
    order.append([2, l2, r2, s2])
    if l1 <= l3:
        order.append([1, l1, r1, s1])
        order.append([3, l3, r3, s3])
    else:
        order.append([3, l3, r3, s3])
        order.append([1, l1, r1, s1])
else:
    order.append([3, l3, r3, s3])
    if l1 <= l2:
        order.append([1, l1, r1, s1])
        order.append([2, l2, r2, s2])
    else:
        order.append([2, l2, r2, s2])
        order.append([1, l1, r1, s1])
# print(order)
a = 4
if order[0][2] >= order[1][1]:  # если 1 заезжает на 2
    if order[1][2] >= order[2][1] or order[0][2] >= order[2][1]:
        a = 5
    else:  # если 3 далеко от 2
        a = order[2][0]
        if order[2][1] - order[1][2] <= order[0][3]:
            if a > order[0][0]:
                a = order[0][0]
        if order[2][1] - order[0][2] <= order[1][3]:
            if a > order[1][0]:
                a = order[1][0]
else:  # если 1 далеко от второй
    if order[1][2] >= order[2][1]:  # если 2 заезжает на 3
        a = order[0][0]
        if order[2][1] - order[0][2] <= order[1][3]:
            if a > order[1][0]:
                a = order[1][0]
        if order[1][1] - order[0][2] <= order[2][3]:
            if a > order[2][0]:
                a = order[2][0]
    else:  # если 1 далеко от 2, а 2 далеко от 3
        if order[1][1] - order[0][2] <= order[2][3]:
            a = order[2][0]
        if order[2][1] - order[1][2] <= order[0][3]:
            if a > order[0][0]:
                a = order[0][0]
if a == 4:
    print('-1')
elif a == 5:
    print('0')
else:
    print(a)
