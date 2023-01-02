from random import randint
from collections import Counter


class Matrix:
    """Matrix constructor"""

    def __init__(self, matrix):
        """
        Initial function, should receive an array that looks like a Matrix
        [[9, 3, 4], [4, -2, 0], [1, 7, 3]]
        """

        self.M = matrix

    def __add__(self, other):
        col, row = self.size.values()
        other_col, other_row = other.size.values()

        return self.__addition(other.value) if col == other_col and row == other_row else None

    def __mul__(self, other):
        col, row = self.size.values()
        other_col, other_row = other.size.values()

        return self.__multiplictation(other.value, {'col': other_col, 'row': row}) if col == other_row else None

    def __str__(self):
        """Print Matrix as a nice formatted way."""

        txt = "[{result}\n]\n"
        r = ""
        for x, arr in enumerate(self.M):
            r += "\n\t{0}".format(arr)
        return txt.format(result=r)

    def __sub__(self, other):
        col, row = other.size.values()
        if col == self.size['col'] and row == self.size['row']:
            return self.__substaction(other.value)
        else:
            return None

    def __eq__(self, other):
        return self.value == other.value

    value = property(lambda self: self.M)

    @property
    def size(self):
        """
        Helper function, return an object that contains numbers of row and col in the current Matrix.
        return {
                col: <int>,
                row: <int>
            }
        """
        c = list(Counter(list(map(lambda x: len(x), self.M))).items())
        return dict(col=(lambda: None, lambda: c[0][0])[len(c) == 1](), row=len(self.M))

    def __addition(self, other):
        result = [[] for x in self.M]

        for i, arr in enumerate(self.M):
            for j, arr_ in enumerate(arr):
                result[i].append(j + other[i][j])

        return Matrix(result)

    def __multiplictation(self, other, size_returned):
        col, row = size_returned.values()
        o = self.M
        p = other
        result = [[0 for x in range(0, col)] for x in range(0, row)]

        for i in range(0, row):
            for j in range(0, col):
                for h, item in enumerate(self.M[i]):
                    result[i][j] += item * other[h][j]

        return Matrix(result)

    def __substaction(self, other):
        result = [[] for x in self.M]

        for i, arr in enumerate(self.M):
            for j, val in enumerate(arr):
                result[i].append(val - other[i][j])

        return Matrix(result)

    def scalar_multiplication(self, constant):
        result = [[] for x in self.M]

        for i, arr in enumerate(self.M):
            for j, val in enumerate(arr):
                result[i].append(constant * val)

        self.M = result
        return Matrix(result)

    def transpose(self):
        col, row = self.size.values()
        result = [[] for x in range(0, col)]

        for i, arr in enumerate(result):
            for item in self.M:
                result[i].append(item[i])

        self.M = result
        return Matrix(result)


A = Matrix([[1, 2], [3, 4]])
B = Matrix([[2, 0], [1, 2]])
C = A - B
D = A + B
E = B * A
F = A == B
scalar_result = A.scalar_multiplication(2)
print("{0}\nA-B = {1}\nA+B = {2}\nA*B = {3}\nA==B = {4}".format(A, C, D, E, F))
