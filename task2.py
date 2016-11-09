import numpy as np


def my_func(x):
    A = []
    for i in range(x.shape[0]):
        A.append(x[i_idx[i], j_idx[i]])
    Z = np.array(A)
    print(Z)


def numpy_func(x, i_idx, j_idx):
    print(x[i_idx, j_idx])


x = np.array(range(4 * 5)).reshape(4, 5) + 1
i_idx = np.array([1, 3, 0, 2])
j_idx = np.array([0, 2, 3, 1])

my_func(x)
numpy_func(x, i_idx, j_idx)
