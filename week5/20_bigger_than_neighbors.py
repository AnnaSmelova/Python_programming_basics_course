# Дан список чисел.
# Определите, сколько в этом списке элементов,
# которые больше двух своих соседей и выведите количество таких элементов.

my_l = list(map(int, input().split()))
kol = 0
s1 = ''
s2 = ''
for i in range(len(my_l)):
    if s1 == '':
        s1 = my_l[i]
    elif s2 == '':
        s2 = s1
        s1 = my_l[i]
    else:
        if s1 > my_l[i] and s1 > s2:
            kol += 1
        s2 = s1
        s1 = my_l[i]
print(kol)
