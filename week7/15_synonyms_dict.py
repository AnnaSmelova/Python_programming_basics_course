# Вам дан словарь, состоящий из пар слов.
# Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны.
# Для одного данного слова определите его синоним.

in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('15_synonyms_dict.txt', 'r', encoding='utf8')

d = {}
lines = in_file.readlines()
n = int(lines[0].strip())
for i in range(1, n + 1):
    string = lines[i].strip().split()
    d[string[1]] = string[0]
    d[string[0]] = string[1]
print(d[lines[n + 1].strip()])
