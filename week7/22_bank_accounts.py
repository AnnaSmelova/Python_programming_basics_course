# Некоторый банк хочет внедрить систему управления счетами клиентов,
# поддерживающую следующие операции:
# Пополнение счета клиента.
# Снятие денег со счета.
# Запрос остатка средств на счете.
# Перевод денег между счетами клиентов.
# Начисление процентов всем клиентам.
# Вам необходимо реализовать такую систему.
# Клиенты банка идентифицируются именами (уникальная строка,
# не содержащая пробелов). Первоначально у банка нет ни одного клиента.
# Как только для клиента проводится операция пополнения, снятия
# или перевода денег, ему заводится счет с нулевым балансом.
# Все дальнейшие операции проводятся только с этим счетом.
# Сумма на счету может быть как положительной,
# так и отрицательной, при этом всегда является целым числом.


def add_sum(di, u_name, num):
    if u_name in di:
        di[u_name] += num
    else:
        di[u_name] = num
    return di


in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('22_bank_accounts.txt', 'r', encoding='utf8')
d = {}
lines = in_file.readlines()
for line in lines:
    string = line.strip().split()
    if string[0] == 'DEPOSIT':
        name, s = string[1], int(string[2])
        d = add_sum(d, name, s)
    elif string[0] == 'WITHDRAW':
        name, s = string[1], int(string[2])
        d = add_sum(d, name, -s)
    elif string[0] == 'BALANCE':
        name = string[1]
        if name in d:
            print(d[name])
        else:
            print('ERROR')
    elif string[0] == 'TRANSFER':
        name1, name2, s = string[1], string[2], int(string[3])
        if name1 not in d:
            d[name1] = 0
        if name2 not in d:
            d[name2] = 0
        d[name1] -= s
        d[name2] += s
    elif string[0] == 'INCOME':
        s = int(string[1])
        for n in d.keys():
            if d[n] > 0:
                p = (d[n] * s) / 100
                d[n] += p
                d[n] = int(d[n])
