import numpy as np


def my_func(x):
    num = []
    cnt = []
    count = 0
    for i in x:
        if not i in num:
            count = 0
            num.append(i)
            for j in x:
                if i == j:
                    count += 1
            cnt.append(count)

    print(num)
    print(cnt)


def numpy_func(x):
    num = np.array(np.unique(x))
    print(np.unique(x))

    cnt = np.bincount(x)
    print(cnt[cnt > 0])


x = np.array([2, 2, 2, 3, 3, 3, 5])
my_func(x)
numpy_func(x)