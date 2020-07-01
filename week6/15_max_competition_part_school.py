# В олимпиаде по информатике принимало участие N человек.
# Определите школы, из которых в олимпиаде принимало участие
# больше всего участников. В этой задаче необходимо считывать
# данные построчно, не сохраняя в памяти данные обо всех участниках,
# а только подсчитывая число участников для каждой школы.

in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('15_max_competition_part_school.txt', 'r', encoding='utf8')

res = [0]*100
lines = in_file.readlines()
for line in lines:
    string = line.strip().split()
    res[int(string[-2]) - 1] += 1
m = max(res)
for i in range(len(res)):
    if res[i] == m:
        print(i + 1, end=' ')
