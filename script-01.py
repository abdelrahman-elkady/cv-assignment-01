import cv2
import numpy as np

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]


def set_pixels(img, pos, rgb):
    row, col = pos
    r, g, b = rgb
    # Set the three channels -- BGR
    img.itemset((row, col, 0), b)
    img.itemset((row, col, 1), g)
    img.itemset((row, col, 2), r)

def get_pixels(img, pos):
    row, col = pos

    b=img.item((row, col, 0))
    g=img.item((row, col, 1))
    r=img.item((row, col, 2))

    return r,g,b


def to_binary(img, threshold=128):
    for i in xrange(len(img)):
        for j in xrange(len(img[i])):
            rgb = get_pixels(img, (i, j))
            avg = np.average(rgb)
            if(avg < threshold):
                set_pixels(img, (i, j), BLACK)
            else:
                set_pixels(img, (i, j), WHITE)


img = cv2.imread('./data/L1.jpg')

to_binary(img)

cv2.imshow("Image", img)

cv2.waitKey(0)
