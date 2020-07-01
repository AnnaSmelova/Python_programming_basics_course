# Известно, что фамилии всех участников — различны.
# Сохраните в массивах список всех участников и выведите его,
# отсортировав по фамилии в лексикографическом порядке.
# При выводе указываете фамилию, имя участника и его балл.
# Используйте для ввода и вывода файлы
# input.txt и output.txt с указанием кодировки utf8.
# Например, для чтения откройте файл с помощью
# open('input.txt', 'r', encoding='utf8').

in_file = open('input.txt', 'r', encoding='utf8')
out_file = open('output.txt', 'w', encoding='utf8')
# in_file = open('08_alphabet_sort_list_input.txt', 'r', encoding='utf8')
# out_file = open('08_alphabet_sort_list_output.txt', 'w', encoding='utf8')

res = []
lines = in_file.readlines()
for line in lines:
    string = line.strip().split()
    res.append((string[0], string[1], string[3]))
res.sort()
for el in res:
    print(*el, file=out_file)
