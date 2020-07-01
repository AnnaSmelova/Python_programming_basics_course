# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга.

result = 'NO'
field = []
for i in range(8):
    s = []
    for j in range(8):
        s.append('.')
    field.append(s)

a = []
b = []
c = []
for _ in range(8):
    h, v = list(map(int, input().split()))
    a.append([h, v])
    if h not in b:
        b.append(h)
    if v not in c:
        c.append(v)
    field[h - 1][v - 1] = '*'

if len(b) < 8 or len(c) < 8:
    result = 'YES'
else:
    for k in a:
        if result == 'YES':
            break
        hor = k[0]
        ver = k[1]
        while hor >= 0 and ver >= 0:
            hor -= 1
            ver -= 1
            if [hor, ver] in a:
                result = 'YES'
                break
        hor = k[0]
        ver = k[1]
        while hor >= 0 and ver <= 7:
            hor -= 1
            ver += 1
            if [hor, ver] in a:
                result = 'YES'
                break
        hor = k[0]
        ver = k[1]
        while hor <= 7 and ver >= 0:
            hor += 1
            ver -= 1
            if [hor, ver] in a:
                result = 'YES'
                break
        hor = k[0]
        ver = k[1]
        while hor <= 7 and ver <= 7:
            hor += 1
            ver += 1
            if [hor, ver] in a:
                result = 'YES'
                break
print(result)
