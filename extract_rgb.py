# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import copy


def main():
    im = Image.open('pic.jpg')
    im = np.array(im)

    plt.subplot(2, 2, 1)
    plt.title('origin image')
    plt.imshow(im)


    im_r = copy.deepcopy(im)
    im_r[:,:,1] = 0
    im_r[:,:,2] = 0
    plt.subplot(2, 2, 2)
    plt.title('R')
    plt.imshow(im_r)
    plt.imsave("pic_rgb_r.jpg", im_r)

    im_g = copy.deepcopy(im)
    im_g[:, :, 0] = 0
    im_g[:, :, 2] = 0
    plt.subplot(2, 2, 3)
    plt.title('G')
    plt.imshow(im_g)
    plt.imsave("pic_rgb_g.jpg", im_g)

    im_b = copy.deepcopy(im)
    im_b[:, :, 0] = 0
    im_b[:, :, 1] = 0
    plt.subplot(2, 2, 4)
    plt.title('B')
    plt.imshow(im_b)
    plt.imsave("pic_rgb_b.jpg", im_b)

    plt.show()


if __name__ == '__main__':
    main()