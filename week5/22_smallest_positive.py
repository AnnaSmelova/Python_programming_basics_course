# Выведите значение наименьшего из всех положительных элементов в списке.
# Известно, что в списке есть хотя бы один положительный элемент,
# а значения всех элементов списка по модулю не превосходят 1000.


my_l = list(map(int, input().split()))
min_el = ''
for i in range(len(my_l)):
    if my_l[i] > 0:
        if min_el == '':
            min_el = my_l[i]
        elif my_l[i] < min_el:
            min_el = my_l[i]
print(min_el)
