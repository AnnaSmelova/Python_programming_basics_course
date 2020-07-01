# В олимпиаде по информатике принимало участие несколько человек.
# Победителем олимпиады становится человек, набравший больше всех баллов.
# Победители определяются независимо по каждому классу.
# Определите количество баллов, которое набрал победитель в каждом классе.
# Гарантируется, что в каждом классе был хотя бы один участник.


in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('11_max_ball.txt', 'r', encoding='utf8')

res = [0, 0, 0]
lines = in_file.readlines()
for line in lines:
    string = line.strip().split()
    if res[int(string[2]) - 9] < int(string[3]):
        res[int(string[2]) - 9] = int(string[3])
print(*res)
