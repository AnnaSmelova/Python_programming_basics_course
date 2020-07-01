# Статья 83 закона “О выборах депутатов Государственной Думы Федерального
# Собрания Российской Федерации” определяет следующий алгоритм
# пропорционального распределения мест в парламенте.
#
# Необходимо распределить 450 мест между партиями, участвовавших в выборах.
# Сначала подсчитывается сумма голосов избирателей, поданных за каждую партию
# и подсчитывается сумма голосов, поданных за все партии.
# Эта сумма делится на 450, получается величина, называемая
# “первое избирательное частное” (смысл первого избирательного частного
# - это количество голосов избирателей, которое необходимо набрать для
# получения одного места в парламенте). Далее каждая партия получает
# столько мест в парламенте, чему равна целая часть от деления числа голосов
# за данную партию на первое избирательное частное.Если после первого раунда
# распределения мест сумма количества мест, отданных партиям, меньше 450,
# то оставшиеся места передаются по одному партиям, в порядке убывания
# дробной части частного от деления числа голосов за данную партию на первое
# избирательное частное. Если же для двух партий эти дробные части равны,
# то преимущество отдается той партии, которая получила большее число голосов.


def sort_func1(elem):
    return elem[4], elem[2]


def sort_func2(elem):
    return elem[0]


in_file = open('input.txt', encoding='UTF8')
# in_file = open('20_election_of_deputies.txt', encoding='UTF8')

lines = in_file.readlines()
kol = 0
s = []
ind = 0
for line in lines:
    string = line.strip().split()
    s.append([ind, ' '.join(string[:-1]), int(string[-1])])
    kol += int(string[-1])
    ind += 1
div_kol = kol / 450
num = 0
for el in s:
    m = int(el[2] // div_kol)
    el.append(m)
    num += m
    el.append(el[2] % div_kol)
ost = 450 - num
if ost != 0:
    s.sort(key=sort_func1, reverse=True)
    j = 0
    while ost != 0 and j < len(s):
        s[j][3] += 1
        ost -= 1
        j += 1
s.sort(key=sort_func2)
for h in s:
    print(h[1], h[3])