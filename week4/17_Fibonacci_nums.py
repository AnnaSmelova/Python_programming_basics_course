# Напишите функцию phib(n), которая по данному целому
# неотрицательному n возвращает n-e число Фибоначчи.
# В этой задаче нельзя использовать циклы - используйте рекурсию.


def phib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return phib(n - 1) + phib(n - 2)

x = int(input())
print(phib(x))
