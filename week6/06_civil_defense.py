# Штаб гражданской обороны Тридесятой области решил обновить план
# спасения на случай ядерной атаки. Известно, что все n селений
# Тридесятой области находятся вдоль одной прямой дороги.
# Вдоль дороги также расположены m бомбоубежищ, в которых жители
# селений могут укрыться на случай ядерной атаки.
# Чтобы спасение в случае ядерной тревоги проходило как можно эффективнее,
# необходимо для каждого селения определить ближайшее к нему бомбоубежище.


def sort_func(elem):
    return elem[1]


n = int(input())
sel = list(map(int, input().split()))
m = int(input())
bom = list(map(int, input().split()))

sel1 = []
for i in range(n):
    sel1.append((i + 1, sel[i]))
sel1.sort(key=sort_func)

bom1 = []
for j in range(m):
    bom1.append((j + 1, bom[j]))
bom1.sort(key=sort_func)

res = []
i, j = 0, 0
k = 1
while k == 1 and i < n:
    k = 0
    if j == 0:
        if sel1[i][1] <= bom1[j][1]:
            res.append((sel1[i][0], bom1[j][0]))
            i += 1
            k = 1
        else:
            if j < m - 1:
                j += 1
                k = 1
            elif j == m - 1:
                res.append((sel1[i][0], bom1[j][0]))
                i += 1
                k = 1
    else:
        if sel1[i][1] <= bom1[j][1]:
            r1 = bom1[j][1] - sel1[i][1]
            r2 = sel1[i][1] - bom1[j - 1][1]
            if r1 < r2:
                res.append((sel1[i][0], bom1[j][0]))
                i += 1
                k = 1
            else:
                res.append((sel1[i][0], bom1[j - 1][0]))
                i += 1
                k = 1
        else:
            if j < m - 1:
                j += 1
                k = 1
            elif j == m - 1:
                res.append((sel1[i][0], bom1[j][0]))
                i += 1
                k = 1
res.sort()
res1 = []
for el in res:
    res1.append(el[1])
print(*res1)
