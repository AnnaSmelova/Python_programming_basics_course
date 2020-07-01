# Дан текст. Выведите все слова, встречающиеся в тексте,
# по одному на каждую строку. Слова должны быть отсортированы
# по убыванию их количества появления в тексте,
# а при одинаковой частоте появления — в лексикографическом порядке.

in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('18_frequency_analysis.txt', 'r', encoding='utf8')

d = {}
lines = in_file.readlines()
for line in lines:
    string = line.strip().split()
    for el in string:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
elem_list = []
for k in d.items():
    elem_list.append((-k[1], k[0]))
elem_list.sort()
for i in elem_list:
    print(i[1])
