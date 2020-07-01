# Циклически сдвиньте элементы списка вправо
# (A[0] переходит на место A[1], A[1] на место A[2], ...,
# последний элемент переходит на место A[0]).

myl = list(map(int, input().split()))
lng = len(myl)
tmp = myl[0]
for i in range(1, lng):
    tmp, myl[i] = myl[i], tmp
myl[0] = tmp
print(*myl)
