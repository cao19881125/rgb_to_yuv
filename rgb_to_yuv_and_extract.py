# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import copy

def rgb_to_ycbcr(im_rgb):
    im_ycbcr = copy.deepcopy(im_rgb)

    R = im_rgb[:, :, 0]
    G = im_rgb[:, :, 1]
    B = im_rgb[:, :, 2]

    im_ycbcr[:, :, 0] = 0.299 * R + 0.587 * G + 0.114 * B
    im_ycbcr[:, :, 1] = -0.1687 * R - 0.3313 * G + 0.5 * B + 128
    im_ycbcr[:, :, 2] = 0.5 * R - 0.4187 * G - 0.0813 * B + 128

    return np.uint8(im_ycbcr)

def ycbcr_to_rgb(im_ycbcr):

    im_rgb = copy.deepcopy(im_ycbcr)

    im_rgb = im_rgb.astype(np.float)

    Y = im_rgb[:, :, 0]
    Cb = im_rgb[:, :, 1] - 128
    Cr = im_rgb[:, :, 2] - 128

    im_result = copy.deepcopy(im_rgb)
    im_result[:, :, 0] = Y + 1.402*Cr
    im_result[:, :, 1] = Y - 0.34414*Cb - 0.71414*Cr
    im_result[:, :, 2] = Y + 1.772*Cb

    return np.uint8(im_result)


def main():
    im = Image.open('pic.jpg')
    im = np.array(im)

    plt.subplot(2, 2, 1)
    plt.title('origin image')
    plt.imshow(im)

    im_ycbcr = rgb_to_ycbcr(im)


    # 输出Y分量，使Cb,Cr分量为128
    im_ycbcr_y = copy.deepcopy(im_ycbcr)
    im_ycbcr_y[:,:,1] = 128
    im_ycbcr_y[:,:,2] = 128

    im_rgb_y = ycbcr_to_rgb(im_ycbcr_y)
    plt.subplot(2, 2, 2)
    plt.title('YCbCr Y')
    plt.imshow(im_rgb_y)
    plt.imsave("pic_ycbcr_y.jpg", im_rgb_y)

    # 输出Cb分量，使Y=0,Cr=0
    im_ycbcr_cb = copy.deepcopy(im_ycbcr)
    im_ycbcr_cb[:, :, 0] = 0
    im_ycbcr_cb[:, :, 2] = 0
    im_rgb_cb = ycbcr_to_rgb(im_ycbcr_cb)
    plt.subplot(2, 2, 3)
    plt.title('YCbCr Cb')
    plt.imshow(im_rgb_cb)
    plt.imsave("pic_ycbcr_cb.jpg", im_rgb_cb)

    # 输出Cr分量，使Y=0,Cb=0
    im_ycbcr_cr = copy.deepcopy(im_ycbcr)
    im_ycbcr_cr[:, :, 0] = 0
    im_ycbcr_cr[:, :, 1] = 0
    im_rgb_cr = ycbcr_to_rgb(im_ycbcr_cr)
    plt.subplot(2, 2, 4)
    plt.title('YCbCr Cr')
    plt.imshow(im_rgb_cr)
    plt.imsave("pic_ycbcr_cr.jpg", im_rgb_cr)

    plt.show()



if __name__ == '__main__':
    main()