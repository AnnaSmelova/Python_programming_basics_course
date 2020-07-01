# Дан список стран и городов каждой страны.
# Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.

in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('13_countries_and_cities.txt', 'r', encoding='utf8')

lines = in_file.readlines()
n = int(lines[0].strip())
d = {}
for i in range(1, n + 1):
    string = lines[i].strip().split()
    for k in range(1, len(string)):
        d[string[k]] = string[0]
m = int(lines[n + 1].strip())
for j in range(n + 2, n + 2 + m):
    print(d[lines[j].strip()])
