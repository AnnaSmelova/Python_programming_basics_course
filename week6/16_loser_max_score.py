# Зачет проводится отдельно в каждом классе.
# Победителями олимпиады становятся школьники,
# которые набрали наибольший балл среди всех участников в данном классе.
# Для каждого класса определите максимальный балл,
# который набрал школьник, не ставший победителем в данном классе.

in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('16_loser_max_score.txt', 'r', encoding='utf8')

res = [0, 0, 0]
prev = [0, 0, 0]
lines = in_file.readlines()
for line in lines:
    string = line.strip().split()
    if res[int(string[2]) - 9] < int(string[3]):
        prev[int(string[2]) - 9] = res[int(string[2]) - 9]
        res[int(string[2]) - 9] = int(string[3])
    elif prev[int(string[2]) - 9] == 0:
        prev[int(string[2]) - 9] = int(string[3])
    elif prev[int(string[2]) - 9] < int(string[3]) \
            and res[int(string[2]) - 9] != int(string[3]):
        prev[int(string[2]) - 9] = int(string[3])
print(*prev)
