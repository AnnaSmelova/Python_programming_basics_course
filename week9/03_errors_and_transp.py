# Добавьте в программу из предыдущей задачи класс MatrixError,
# содержащий внутри self поля matrix1 и matrix2 — ссылки на матрицы.
#
# В класс Matrix внесите следующие изменения:
#
# Добавьте в метод __add__ проверку на ошибки в размере входных данных,
# чтобы при попытке сложить матрицы разных размеров было выброшено исключение MatrixError таким образом,
# чтобы matrix1 поле MatrixError стало первым аргументом __add__ (просто self),
# а matrix2 — вторым (второй операнд для сложения).
# Реализуйте метод transpose, транспонирующий матрицу и возвращающую результат
# (данный метод модифицирует экземпляр класса Matrix)
# Реализуйте статический метод transposed, принимающий Matrix и возвращающий транспонированную матрицу.

from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


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
        if self.size() == other.size():
            result = []
            body_lng = len(self.body)
            for k in range(body_lng):
                line = []
                k_lng = len(self.body[k])
                for i in range(k_lng):
                    line.append(self.body[k][i] + other.body[k][i])
                result.append(line)
        else:
            raise MatrixError(self, other)
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

    __rmul__ = __mul__

    def transpose(self):
        self.body = list(map(list, zip(*self.body)))
        return self

    @staticmethod
    def transposed(matrix):
        body1 = deepcopy(matrix.body)
        body1 = list(map(list, zip(*body1)))
        return Matrix(body1)

exec(stdin.read())
