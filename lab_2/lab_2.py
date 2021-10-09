import numpy as np
from time import perf_counter

from matrix import Matrix


def numpy_multiply(matrix1, matrix2):
    return np.dot(matrix1, matrix2)


if __name__ == '__main__':
    matrix1 = Matrix.generate_random_matrix((500, 600))
    matrix2 = Matrix.generate_random_matrix((600, 500))
    np_matrix1 = matrix1.to_numpy()
    np_matrix2 = matrix2.to_numpy()
    start = perf_counter()
    result = matrix1 * matrix2
    print("Without numpy: {}".format(perf_counter()-start))
    start = perf_counter()
    result_with_np = numpy_multiply(np_matrix1, np_matrix2)
    print("With numpy: {}".format(perf_counter()-start))