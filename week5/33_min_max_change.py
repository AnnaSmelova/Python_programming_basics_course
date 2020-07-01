# В списке все элементы попарно различны.
# Поменяйте местами минимальный и максимальный элемент этого списка.

myl = list(map(int, input().split()))
ma = myl[0]
ma_ind = 0
mi = myl[0]
mi_ind = 0
for i in range(1, len(myl)):
    if myl[i] > ma:
        ma = myl[i]
        ma_ind = i
    elif myl[i] < mi:
        mi = myl[i]
        mi_ind = i
myl[mi_ind], myl[ma_ind] = myl[ma_ind], myl[mi_ind]
print(*myl)
