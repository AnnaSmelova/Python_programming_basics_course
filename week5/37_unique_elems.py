# Дан список. Выведите те его элементы,
# которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

a = list(map(int, input().split()))
b = a.copy()
c = []
for el in a:
    b.remove(el)
    if el not in b and el not in c:
        print(el, end=' ')
    c.append(el)
