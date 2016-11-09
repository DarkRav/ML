import numpy as np


def my_func(x):
    result = []
    count = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[0] - 1):
            if i == j:
                if x[i, j] > 0:
                    result.append(x[i, j])
                    count += 1
    if count == 0:
        print(0)
    elif count == 1:
        print(result[0])
    else:
        num = 1
        for i in result:
            num = num * i
        print(num)


def numpy_func(x):
    d = x.diagonal()
    s = np.multiply.reduce(d[d > 0])
    print(s)


x = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])
my_func(x)
numpy_func(x)
