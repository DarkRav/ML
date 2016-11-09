import numpy as np


def compare(x, y):
    for i in range(x.shape[0]):
        if x[i] == y[i]:
            if i == 3:
                return "is multiset"
        else:
            return "not multiset"


def my_func(x, y):
    tmp = 0
    for j in range(x.shape[0]):
        for i in range(x.shape[0] - 1):
            if y[i] > y[i + 1]:
                tmp = y[i]
                y[i] = y[i + 1]
                y[i + 1] = tmp

            if x[i] > x[i + 1]:
                tmp = x[i]

    tmp = 0
    for j in range(x.shape[0]):
        for i in range(x.shape[0] - 1):
            if y[i] > y[i + 1]:
                tmp = y[i]
                y[i] = y[i + 1]
                y[i + 1] = tmp

            if x[i] > x[i + 1]:
                tmp = x[i]
                x[i] = x[i + 1]
                x[i + 1] = tmp

    print(compare(x, y))


def numpy_func(x, y):
    print(np.array_equal(x, y))


X = np.array([1, 2, 2, 4])
Y = np.array([4, 2, 2, 1])

my_func(X, Y)
numpy_func(X, Y)
