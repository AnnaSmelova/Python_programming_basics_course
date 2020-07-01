# Даны числа a, b, c, d, e. Подсчитайте количество таких целых чисел
# от 0 до 1000 (включительно), которые являются корнями уравнения
# (ax³+bx²+cx+d)/(x-e)=0, и выведите их количество.

a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())

num = 0

for i in range(0, 1001):
    if i != e:
        if a * i**3 + b * i**2 + c * i + d == 0:
            num += 1
print(num)
