# Дан список чисел. Выведите значение наибольшего элемента в списке,
# а затем индекс этого элемента в списке.
# Если наибольших элементов несколько,
# выведите их значение и индекс первого из них.

my_l = list(map(int, input().split()))
max_el = my_l[0]
ind = 0
for i in range(len(my_l)):
    if my_l[i] > max_el:
        max_el = my_l[i]
        ind = i
print(max_el, ind)
