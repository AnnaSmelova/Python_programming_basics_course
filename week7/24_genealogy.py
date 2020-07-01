# В генеалогическом древе у каждого человека, кроме родоначальника,
# есть ровно один родитель. Каждом элементу дерева сопоставляется целое
# неотрицательное число, называемое высотой. У родоначальника высота равна 0,
# у любого другого элемента высота на 1 больше, чем у его родителя.
# Вам дано генеалогическое древо, определите высоту всех его элементов.

n = int(input())
d = {}
s = set()
for _ in range(n - 1):
    string = input().split()
    s.add(string[0])
    s.add(string[1])
    if string[0] in d:
        d[string[0]].append(string[1])
    else:
        d[string[0]] = [string[1]]
s = sorted(list(s))
for name in s:
    name_p = name
    lev = 0
    while name in d.keys():
        lev += 1
        name = d[name][0]
    print(name_p, lev)
