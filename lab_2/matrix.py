import random
from typing import List, Tuple, Union

import numpy as np


class Matrix:
    def __init__(self, matrix: List[List[float]]):
        self._matrix = matrix
        self._shape = len(matrix), len(matrix[0])

    @classmethod
    def generate_random_matrix(cls, shape: Tuple[int, int]):
        matrix = [[random.random() for _ in range(shape[1])] for _ in range(shape[0])]
        return cls(matrix)

    @staticmethod
    def multiply_rows(row1: List[Union[float, int]], row2: List[Union[float, int]]):
        return sum(el1*el2 for el1, el2 in zip(row1, row2))

    def to_numpy(self):
        return np.asarray([np.asarray(row) for row in self._matrix])

    def __getitem__(self, item):
        if not isinstance(item, int) and len(item) > 1:
            result = list(map(lambda x: x[item[1]], self._matrix))
            return result
        return self._matrix[item]

    def __mul__(self, other: 'Matrix'):
        shape = (self._shape[0], other._shape[1])
        result = [[0 for _ in range(shape[1])] for _ in range(shape[0])]
        if isinstance(other, Matrix):
            for i in range(shape[0]):
                for j in range(shape[1]):
                    result[i][j] = Matrix.multiply_rows(self[i], other[:, j])
            return Matrix(result)

    def __str__(self):
        result = ""
        for row in self._matrix:
            result += " ".join(map(str, row))
            result += "\n"
        return result
