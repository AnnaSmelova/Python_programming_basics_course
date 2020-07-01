# В Государственную Думу Федерального Собрания Российской Федерации
# выборы производятся по партийным спискам.
# Каждый избиратель указывает одну партию, за которую он отдает свой голос.
# В Государственную Думу попадают партии,
# которые набрали не менее 7% от числа голосов избирателей.
# Дан список партий и список голосов избирателей.
# Выведите список партий, которые попадут в Государственную Думу.

in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('18_7_percent.txt', 'r', encoding='utf8')

p = []
v = []
k = 0
kol = 0
lines = in_file.readlines()
for i in range(1, len(lines)):
    string = lines[i].strip()
    if string == 'VOTES:':
        k = 1
    if k == 0:
        p.append(string)
        v.append(0)
    elif string != 'VOTES:':
        kol += 1
        for j in range(len(p)):
            if string == p[j]:
                v[j] += 1
                break
for d in range(len(v)):
    per = (v[d] * 100) / kol
    if per >= 7:
        print(p[d])
