# Каждый из N школьников некоторой школы знает Mᵢ языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.

in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('09_polyglots.txt', 'r', encoding='utf8')

lines = in_file.readlines()
n = int(lines[0].strip())
common_set = set()
all_set = set()
m = int(lines[1].strip())
for k in range(m):
    common_set.add(lines[k + 2].strip())
    all_set.add(lines[k + 2].strip())
i = m + 2
kol = 2
while kol <= n:
    kol += 1
    h = int(lines[i].strip())
    loc = set()
    for k in range(h):
        common_set.add(lines[i + 1 + k].strip())
        loc.add(lines[i + 1 + k].strip())
    all_set &= loc
    i += h + 1
print(len(all_set))
all_set = list(all_set)
all_set.sort()
for el in all_set:
    print(el)
print(len(common_set))
common_set = list(common_set)
common_set.sort()
for el in common_set:
    print(el)
