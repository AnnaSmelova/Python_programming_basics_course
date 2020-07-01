# Добавьте в предыдущий класс следующие методы:
#
# __add__, принимающий вторую матрицу того же размера и возвращающий сумму матриц.
# __mul__, принимающий число типа int или float и возвращающий матрицу,
# умноженную на скаляр.
# __rmul__, делающий то же самое, что и __mul__.
# Этот метод будет вызван в том случае, аргумент находится справа.
# Для реализации этого метода в коде класса достаточно написать __rmul__ = __mul__.


from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, matr):
        self.body = deepcopy(matr)

    def __str__(self):
        result = ''
        body_lng = len(self.body)
        for k in range(body_lng):
            k_lng = len(self.body[k])
            for i in range(k_lng):
                result += str(self.body[k][i])
                if i != k_lng - 1:
                    result += '\t'
                elif k != body_lng - 1:
                    result += '\n'
        return result

    def size(self):
        return len(self.body), len(self.body[0])

    def __add__(self, other):
        result = []
        body_lng = len(self.body)
        for k in range(body_lng):
            line = []
            k_lng = len(self.body[k])
            for i in range(k_lng):
                line.append(self.body[k][i] + other.body[k][i])
            result.append(line)
        return Matrix(result)

    def __mul__(self, other):
        result = []
        body_lng = len(self.body)
        for k in range(body_lng):
            line = []
            k_lng = len(self.body[k])
            for i in range(k_lng):
                line.append(self.body[k][i] * other)
            result.append(line)
        return Matrix(result)

    def __rmul__(self, other):
        return self.__mul__(other)


exec(stdin.read())
