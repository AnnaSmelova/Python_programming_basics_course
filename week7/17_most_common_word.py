# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько,
# выведите то, которое меньше в лексикографическом порядке.

in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('17_most_common_word.txt', 'r', encoding='utf8')

d = {}
p = {}
m = 1
p[1] = []
lines = in_file.readlines()
for line in lines:
    string = line.strip().split()
    for k in string:
        if k in d:
            d[k] += 1
            if d[k] > m:
                m = d[k]
                p[m] = [k]
            elif d[k] == m:
                p[m].append(k)
        else:
            d[k] = 1
            p[1].append(k)
print(sorted(p[sorted(p.keys(), reverse=True)[0]])[0])
