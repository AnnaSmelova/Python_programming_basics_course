# В условиях предыдущей задачи определите количество школьников,
# ставших победителями в каждом классе.
# Победителями объявляются все,
# кто набрал наибольшее число баллов по данному классу.
# Гарантируется, что в каждом классе был хотя бы один участник.

in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('11_max_ball.txt', 'r', encoding='utf8')

res = [0, 0, 0]
kol = [0, 0, 0]
lines = in_file.readlines()
for line in lines:
    string = line.strip().split()
    if res[int(string[2]) - 9] < int(string[3]):
        res[int(string[2]) - 9] = int(string[3])
        kol[int(string[2]) - 9] = 1
    elif res[int(string[2]) - 9] == int(string[3]):
        kol[int(string[2]) - 9] += 1
print(*kol)
