# Дана база данных о продажах некоторого интернет-магазина.
# Каждая строка входного файла представляет собой запись вида
# Покупатель товар количество, где
# Покупатель — имя покупателя (строка без пробелов),
# товар — название товара (строка без пробелов),
# количество — количество приобретенных единиц товара.
# Создайте список всех покупателей, а для каждого покупателя
# подсчитайте количество приобретенных им единиц каждого вида товаров.

in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('21_sales.txt', 'r', encoding='utf8')
d = {}
lines = in_file.readlines()
for line in lines:
    string = line.strip().split()
    if string[0] in d:
        if string[1] in d[string[0]]:
            d[string[0]][string[1]] += int(string[2])
        else:
            d[string[0]][string[1]] = int(string[2])
    else:
        p = {}
        p[string[1]] = int(string[2])
        d[string[0]] = p
for el in sorted(d.keys()):
    print(el, ':', sep='')
    for elem in sorted(d[el].keys()):
        print(elem, d[el][elem])
