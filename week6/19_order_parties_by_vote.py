# Формат входных данных аналогичен предыдущей задаче.
# Выведите список всех партий, участвовавших в выборах,
# отсортировав его в порядке убывания количества голосов избирателей,
# а при равном количестве голосов - в лексикографическом порядке.

in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('18_7_percent.txt', 'r', encoding='utf8')

p = []
k = 0
lines = in_file.readlines()
for i in range(1, len(lines)):
    string = lines[i].strip()
    if string == 'VOTES:':
        k = 1
    if k == 0:
        p.append([0, string])
    elif string != 'VOTES:':
        for j in range(len(p)):
            if string == p[j][1]:
                p[j][0] += 1
                break
p.sort(key=lambda x: (-int(x[0]), x[1]))
for el in p:
    print(el[1])
