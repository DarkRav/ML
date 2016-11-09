import numpy as np


def my_func(x):
    max = 0
    for i in range(x.shape[0] - 1):
        if x[i] == 0:
            if x[i + 1] > max:
                max = x[i + 1]
    print(max)


def numpy_func(x):
    zero = x == 0
    print(x[1:][zero[:-1]].max())


x = np.array([0, 2, 0, 3, 0, 0, 5, 7, 0])
my_func(x)
numpy_func(x)
