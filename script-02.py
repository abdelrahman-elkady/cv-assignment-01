import cv2
import numpy as np
import math


def set_pixels(img, pos, rgb):
    row, col = pos
    r, g, b = rgb
    # Set the three channels -- BGR
    img.itemset((row, col, 0), b)
    img.itemset((row, col, 1), g)
    img.itemset((row, col, 2), r)


def get_pixels(img, pos):
    row, col = pos

    b = img.item((row, col, 0))
    g = img.item((row, col, 1))
    r = img.item((row, col, 2))

    return r, g, b


def blend(img_a, img_b, ratio = 0.8):
    height, width, channels = img_a.shape
    dest_img = np.zeros((height, width,channels), np.uint8)

    b = 1 - ratio

    for i in xrange(len(img_a)):
        for j in xrange(len(img_a[i])):

            rgb_a = get_pixels(img_a, (i,j))
            rgb_b = get_pixels(img_b, (i,j))

            rgb_a = map(lambda p: p * ratio, rgb_a)
            rgb_b = map(lambda p: p * b, rgb_b)
            rgb_final = [sum(elem) for elem in zip(rgb_a,rgb_b)]

            set_pixels(dest_img, (i,j), rgb_final)

    return dest_img

img = cv2.imread('./data/L2.jpg')
logo = cv2.imread('./data/logo.jpg')
height, width, _ = img.shape
logo_resized = cv2.resize(logo,(width, height) )

res = blend(img, logo_resized)

cv2.imshow("Image", res)

cv2.waitKey(0)
