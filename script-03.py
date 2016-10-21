import cv2
import numpy as np


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


def change_brightness(img, factor=1.5):
    for i in xrange(len(img)):
        for j in xrange(len(img[i])):
            r, g, b = get_pixels(img, (i, j))
            r *= factor
            g *= factor
            b *= factor
            set_pixels(img, (i, j), [r, g, b])


img = cv2.imread('./data/L2.jpg')
img_before = cv2.imread('./data/L2.jpg')
change_brightness(img)

cv2.imshow("Image-Before", img_before)
cv2.imshow("Image", img)

cv2.waitKey(0)
