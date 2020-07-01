# Август и Беатриса играют в игру.
# Август загадал натуральное число от 1 до n.
# Беатриса пытается угадать это число,
# для этого она называет некоторые множества натуральных чисел.
# Август отвечает Беатрисе YES,
# если среди названных ею чисел есть задуманное или
# NO в противном случае. После нескольких заданных вопросов
# Беатриса запуталась в том, какие вопросы она задавала и
# какие ответы получила и просит вас помочь ей определить,
# какие числа мог задумать Август.

in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('07_guess_num.txt', 'r', encoding='utf8')

lines = in_file.readlines()
a = []
n = int(lines[0])
res = set(range(1, n + 1))
i = 1
while lines[i].strip() != 'HELP':
    if i % 2 == 1:
        string = set(map(int, lines[i].strip().split()))
        a = string
    else:
        string = lines[i].strip()
        if string == 'YES':
            res &= a
        else:
            res -= a
    i += 1
res = list(res)
res.sort()
print(*res)
