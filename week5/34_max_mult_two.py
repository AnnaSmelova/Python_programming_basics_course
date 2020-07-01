# Дан список, заполненный произвольными целыми числами.
# Найдите в этом списке два числа, произведение которых максимально.
# Выведите эти числа в порядке неубывания.
# Решение должно иметь сложность O(n), где n - размер списка.
# То есть сортировку использовать нельзя.

myl = list(map(int, input().split()))
a = []
ama = False
ama2 = False
b = []
bmi = False
bmi2 = False
for el in myl:
    if el >= 0:
        a.append(el)
    else:
        b.append(el)
if len(a) >= 2:
    ama = max(a)
    a.remove(ama)
    ama = str(ama)
    ama2 = str(max(a))
if len(b) >= 2:
    bmi = min(b)
    b.remove(bmi)
    bmi = str(bmi)
    bmi2 = str(min(b))
if ama and ama2 and bmi and bmi2:
    if int(ama) * int(ama2) >= int(bmi) * int(bmi2):
        print(ama2, ama)
    else:
        print(bmi, bmi2)
else:
    if ama and ama2:
        print(ama2, ama)
    elif bmi and bmi2:
        print(bmi, bmi2)
    else:
        if a and b:
            print(b[0], a[0])
