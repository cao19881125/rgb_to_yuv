# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


image = Image.open('pic.jpg')

plt.subplot(2, 3, 1)
plt.title('origin image')
plt.imshow(image)


cmyk_image = image.convert('CMYK')


# 输出C分量
im_c = np.array(cmyk_image)

im_c[:,:,1] = 0
im_c[:,:,2] = 0
im_c[:,:,3] = 0

image_cmyk_c = Image.fromarray(im_c,mode='CMYK')
image_rgb_c = image_cmyk_c.convert('RGB')

plt.subplot(2, 3, 2)
plt.title('cmyk c')
plt.imshow(image_rgb_c)
plt.imsave("pic_cmyk_c.jpg", np.array(image_rgb_c))

# 输出M分量
im_m = np.array(cmyk_image)

im_m[:,:,0] = 0
im_m[:,:,2] = 0
im_m[:,:,3] = 0

image_cmyk_m = Image.fromarray(im_m,mode='CMYK')
image_rgb_m = image_cmyk_m.convert('RGB')

plt.subplot(2, 3, 3)
plt.title('cmyk m')
plt.imshow(image_rgb_m)
plt.imsave("pic_cmyk_m.jpg", np.array(image_rgb_m))

# 输出Y分量
im_y = np.array(cmyk_image)

im_y[:,:,0] = 0
im_y[:,:,1] = 0
im_y[:,:,3] = 0

image_cmyk_y = Image.fromarray(im_y,mode='CMYK')
image_rgb_y = image_cmyk_y.convert('RGB')

plt.subplot(2, 3, 4)
plt.title('cmyk y')
plt.imshow(image_rgb_y)
plt.imsave("pic_cmyk_y.jpg", np.array(image_rgb_y))


# 输出K分量
im_k = np.array(cmyk_image,dtype=np.float)
print(im_k[:,:,3])

im_k[:,:,0] = 0
im_k[:,:,1] = 0
im_k[:,:,2] = 0

image_cmyk_k = Image.fromarray(im_k,mode='CMYK')
image_rgb_k = image_cmyk_k.convert('RGB')

plt.subplot(2, 3, 5)
plt.title('cmyk k')
plt.imshow(image_rgb_k)
plt.imsave("pic_cmyk_k.jpg", np.array(image_rgb_k))

plt.show()




