# В обувном магазине продается обувь разного размера.
# Известно, что одну пару обуви можно надеть на другую,
# если она хотя бы на три размера больше.
# В магазин пришел покупатель.
# Требуется определить, какое наибольшее количество
# пар обуви сможет предложить ему продавец так,
# чтобы он смог надеть их все одновременно.


def count_shoes(start, l):
    kol = 0
    local_start = start
    pr = 0
    if start < l[0]:
        local_start = l[0]
    for k in l:
        if k >= local_start:
            if kol == 0:
                kol += 1
                pr = k
            else:
                if k - pr >= 3:
                    kol += 1
                    pr = k
    return kol


n = int(input())
l = list(map(int, input().split()))
l.sort()

lng = len(l)
if n > l[lng - 1]:
    print(0)
else:
    print(count_shoes(n, l))
