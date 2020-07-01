# В выборах Президента Российской Федерации побеждает кандидат,
# набравший свыше половины числа голосов избирателей.
# Если такого кандидата нет, то во второй тур выборов выходят
# два кандидата, набравших наибольшее число голосов.

in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('19_presidential_elections.txt', 'r', encoding='utf8')
out_file = open('output.txt', 'w', encoding='utf8')
# out_file = open('19_presidential_elections_out.txt', 'w', encoding='utf8')


text = in_file.read().splitlines()

kol = 0
d = {}

for el in text:
    if el in d:
        d[el] += 1
    else:
        d[el] = 1
    kol += 1
pol_kol = kol / 2
mas = []
stop = 0
for name in d.keys():
    if d[name] > pol_kol:
        print(name, file=out_file)
        stop = 1
        break
    else:
        mas.append((-d[name], name))
if stop == 0:
    mas.sort()
    for k in range(2):
        print(mas[k][1], file=out_file)
out_file.close()
