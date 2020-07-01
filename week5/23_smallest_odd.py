# Выведите значение наименьшего нечетного элемента списка,
# гарантируется, что хотя бы один нечётный элемент в списке есть.

myl = list(map(int, input().split()))
sm = ''
for i in range(len(myl)):
    if myl[i] % 2 == 1:
        if sm == '':
            sm = myl[i]
        elif myl[i] < sm:
            sm = myl[i]
print(sm)
