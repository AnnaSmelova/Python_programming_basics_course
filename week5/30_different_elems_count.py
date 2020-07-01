# Дан список, упорядоченный по неубыванию элементов в нем.
# Определите, сколько в нем различных элементов.

myl = list(map(int, input().split()))
kol = 1
pr = myl[0]
for i in range(1, len(myl)):
    if myl[i] != pr:
        kol += 1
        pr = myl[i]
print(kol)
