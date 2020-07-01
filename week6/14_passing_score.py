# Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов
# в виде ЕГЭ, каждый из них оценивается целым числом от 0 до 100 баллов.
# При этом абитуриенты, набравшие менее 40 баллов(неудовлетворительную оценку)
# по любому экзамену из конкурса выбывают. Остальные абитуриенты участвуют
# в конкурсе по сумме баллов за три экзамена.
#
# В конкурсе участвует N человек, при этом количество мест равно K.
# Определите проходной балл, то есть такое количество баллов,
# что количество участников, набравших столько или больше баллов
# не превосходит K, а при добавлении к ним абитуриентов,
# набравших наибольшее количество баллов среди непринятых абитуриентов,
# общее число принятых абитуриентов станет больше K.

in_file = open('input.txt', 'r', encoding='utf8')
out_file = open('output.txt', 'w', encoding='utf8')
# in_file = open('14_passing_score_input.txt', 'r', encoding='utf8')
# out_file = open('14_passing_score_output.txt', 'w', encoding='utf8')


lines = in_file.readlines()
k = int(lines[0])
res = []
for i in range(1, len(lines)):
    string = lines[i].strip().split()
    a, b, c = int(string[-1]), int(string[-2]), int(string[-3])
    if a >= 40 and b >= 40 and c >= 40:
        res.append(a + b + c)
if k == 0:
    print(1, file=out_file)
elif len(res) <= k:
    print(0, file=out_file)
else:
    res.sort(reverse=True)
    if res[k - 1] != res[k]:
        print(res[k - 1], file=out_file)
    else:
        r = k - 1
        while r > 0 and res[r - 1] == res[r]:
            r -= 1
        if r != 0:
            print(res[r - 1], file=out_file)
        else:
            print(1, file=out_file)
