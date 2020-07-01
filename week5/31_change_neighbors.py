# Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.

myl = list(map(int, input().split()))
lng = len(myl)
for i in range(0, lng, 2):
    if i < lng - 1:
        myl[i], myl[i + 1] = myl[i + 1], myl[i]
print(*myl)
