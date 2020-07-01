# Напишите функцию xor(x, y)
# реализующую функцию "Исключающее ИЛИ" двух логических переменных x и y.
# Функция xor должна возвращать True,
# если ровно один из ее аргументов x или y,
# но не оба одновременно равны True.


def xor(a, b):
    return a and not b or b and not a


x, y = int(input()), int(input())
print(int(xor(x, y)))
