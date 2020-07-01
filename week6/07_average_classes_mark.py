# В олимпиаде по информатике принимало участие несколько человек.
# Определите и выведите средние баллы участников олимпиады
# в 9 классе, в 10 классе, в 11 классе.

in_file = open('input.txt', 'r', encoding='utf-8')
# in_file = open('07_average_classes_mark_input.txt', 'r', encoding='utf-8')
lines = in_file.readlines()
marks = [[0, 0], [0, 0], [0, 0]]
for line in lines:
    string = line.strip().split()
    marks[int(string[2]) - 9][0] += int(string[3])
    marks[int(string[2]) - 9][1] += 1
for k in marks:
    print(k[0] / k[1], end=' ')
