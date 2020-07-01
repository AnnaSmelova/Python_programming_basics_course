# Дан список чисел.
# Если в нем есть два соседних элемента одного знака, выведите эти числа.
# Если соседних элементов одного знака нет - не выводите ничего.
# Если таких пар соседей несколько - выведите первую пару.


def get_sign(a):
    if a > 0:
        return 1
    elif a == 0:
        return 0
    else:
        return -1


def one_sign_pair(l):
    pr = ''
    sign = 2
    for i in range(len(l)):
        if pr != '':
            if get_sign(l[i]) == sign:
                return pr, l[i]
        pr = l[i]
        sign = get_sign(l[i])
    return ''


my_l = list(map(int, input().split()))
print(*one_sign_pair(my_l))
