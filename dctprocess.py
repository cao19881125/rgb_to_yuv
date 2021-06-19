# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import copy
import cv2

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
    im = Image.open('camp.jpg')
    im = np.array(im)

    im_ycbcr = rgb_to_ycbcr(im)

    im_ycbcr_y = copy.deepcopy(im_ycbcr)
    im_ycbcr_y[:, :, 1] = 128
    im_ycbcr_y[:, :, 2] = 128

    im_rgb_y = ycbcr_to_rgb(im_ycbcr_y)

    plt.subplot(2, 3, 1)
    plt.imshow(im_rgb_y)
    plt.imsave("dct_trans/camp_origin_image.jpg", im_rgb_y)

    # 变成高低频的热度图
    dct_ycbcr_y_log = copy.deepcopy(im_ycbcr_y)
    img_dct_y = cv2.dct(dct_ycbcr_y_log[:, :, 0].astype('float'))
    img_dct_y_log= np.log(abs(img_dct_y))

    plt.subplot(2, 3, 2)
    plt.imshow(img_dct_y_log)
    plt.imsave("dct_trans/camp_dct_log.jpg", img_dct_y_log)

    # 输出1/4
    dct_ycbcr_y1_4 = copy.deepcopy(im_ycbcr_y)
    img_dct1_4 = cv2.dct(dct_ycbcr_y1_4[:,:,0].astype('float'))
    for m in range(256):
        for n in range(256):
            if m >= 75 and n >= 331 - m:
                img_dct1_4[m, n] = 0
    dct_ycbcr_y1_4[:, :, 0]= cv2.idct(img_dct1_4)

    im_dct_rgb_y1_4 = ycbcr_to_rgb(dct_ycbcr_y1_4)

    plt.subplot(2, 3, 3)
    plt.imshow(im_dct_rgb_y1_4)
    plt.imsave("dct_trans/camp_1_4_image.jpg", im_dct_rgb_y1_4)

    # 输出1/2
    dct_ycbcr_y1_2 = copy.deepcopy(im_ycbcr_y)
    img_dct1_2 = cv2.dct(dct_ycbcr_y1_2[:, :, 0].astype('float'))
    for m in range(256):
        for n in range(256):
            if n >= 256 - m:
                img_dct1_2[m, n] = 0
    dct_ycbcr_y1_2[:, :, 0] = cv2.idct(img_dct1_2)

    im_dct_rgb_y1_2 = ycbcr_to_rgb(dct_ycbcr_y1_2)

    plt.subplot(2, 3, 4)
    plt.imshow(im_dct_rgb_y1_2)
    plt.imsave("dct_trans/camp_1_2_image.jpg", im_dct_rgb_y1_2)

    # 输出3/4
    dct_ycbcr_y3_4 = copy.deepcopy(im_ycbcr_y)
    img_dct3_4 = cv2.dct(dct_ycbcr_y3_4[:, :, 0].astype('float'))
    for m in range(256):
        for n in range(256):
            if not (m < 181 and n < (181 - m)):
                img_dct3_4[m, n] = 0
    dct_ycbcr_y3_4[:, :, 0] = cv2.idct(img_dct3_4)

    im_dct_rgb_y3_4 = ycbcr_to_rgb(dct_ycbcr_y3_4)

    plt.subplot(2, 3, 5)
    plt.imshow(im_dct_rgb_y3_4)
    plt.imsave("dct_trans/camp_3_4_image.jpg", im_dct_rgb_y3_4)

    # 输出7/8
    dct_ycbcr_y7_8 = copy.deepcopy(im_ycbcr_y)
    img_dct7_8 = cv2.dct(dct_ycbcr_y7_8[:, :, 0].astype('float'))
    for m in range(256):
        for n in range(256):
            if not (m < 91 and n < (91 - m)):
                img_dct7_8[m, n] = 0
    dct_ycbcr_y7_8[:, :, 0] = cv2.idct(img_dct7_8)

    im_dct_rgb_y7_8 = ycbcr_to_rgb(dct_ycbcr_y7_8)

    plt.subplot(2, 3, 6)
    plt.imshow(im_dct_rgb_y7_8)
    plt.imsave("dct_trans/camp_7_8_image.jpg", im_dct_rgb_y7_8)

    plt.show()

if __name__ == '__main__':
    main()