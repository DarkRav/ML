import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def my_func():
    img = mpimg.imread('red_panda.png')
    h = img.shape[0]
    w = img.shape[1]

    numChannels = np.array([0.299, 0.587, 0.144])

    x = []
    y = []

    for i in range(h):
        for j in range(w):
            x.append(img[i, j, 0] * numChannels[0] + img[i, j, 1] * numChannels[1] + img[i, j, 2] * numChannels[2])
        y.append(x)
        x = []

    y = np.array(y)

    plt.imshow(y, cmap='gray')
    plt.show()


my_func()