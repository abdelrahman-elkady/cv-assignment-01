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


def homography_transformation(img, pts):
    height, width, channels = img.shape
    src = np.float32(pts)
    dst = np.float32([[0,0], [width - 1, 0], [width -1 , height -1], [0, height - 1]])

    out, _ = cv2.findHomography(src, dst)
    res = cv2.warpPerspective(img, out, (width, height))

    return res


img = cv2.imread('./data/L4.jpg')
res = homography_transformation(img, [[55, 56], [185, 23], [185, 145], [56, 182]])

cv2.imshow("Image", res)

cv2.waitKey(0)
