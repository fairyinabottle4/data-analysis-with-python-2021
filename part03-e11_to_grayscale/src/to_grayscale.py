#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(image):
    return np.dot(image[...,:3], [0.2126, 0.7152, 0.0722])

def to_red(image):
    cpy = image.copy()
    cpy[:, :, 1:] = 0
    #alternatively:
    # multiplicators = [1, 0, 0]
    # return image * multiplicators
    return cpy

def to_green(image):
    cpy = image.copy()
    cpy[:, :, (0,2)] = 0
    #alternatively:
    # multiplicators = [0, 1, 0]
    # return image * multiplicators
    return cpy

def to_blue(image):
    cpy = image.copy()
    cpy[:, :, 0:2] = 0
    #alternatively:
    # multiplicators = [0, 0, 1]
    # return image * multiplicators
    return cpy



def main():
    image = plt.imread("src/painting.png")
    result = to_grayscale(image)
    plt.imshow(result, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    fig, ax = plt.subplots(3,1)
    ax[0].imshow(to_red(image))
    ax[1].imshow(to_green(image))
    ax[2].imshow(to_blue(image))
    plt.show()

if __name__ == "__main__":
    main()
