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


def gen_three_by_three_mat(a, b, c, d, e, f, g, h, i):
    return '%d, %d, %d; %d, %d, %d; %d, %d, %d' % (a, b, c, d, e, f, g, h, i)


def affine_transformation(img, pts):
    pt1_src, pt2_src, pt3_src = pts
    height, width, channels = img.shape

    pt1_dest = (0, 0)
    pt2_dest = (0, height - 1)
    pt3_dest = (width - 1, height - 1)

    mat = gen_three_by_three_mat(pt1_dest[0], pt1_dest[1], 1, pt2_dest[
        0], pt2_dest[1], 1, pt3_dest[0], pt3_dest[1], 1)

    m = np.matrix(mat)
    m_inverse = np.linalg.inv(m)

    a1 = np.dot(m_inverse, m[:, 0])
    a2 = np.dot(m_inverse, m[:, 1])
    a3 = np.dot(m_inverse, m[:, 2])

    affine = np.concatenate((a1, a2, a3))

    result = np.zeros((height, width, channels), np.uint8)

    for i in xrange(len(img)):
        for j in xrange(len(img[i])):
            current = np.matrix('%d %d %d' % (i, j, 1))
            mat_product = np.dot(affine, current)
            print(i,j)
            x = int(max(0, min(math.floor(mat_product[0, 0]), width - 1)))
            y = int(max(0, min(math.floor(mat_product[1, 0]), height - 1)))

            rgb = get_pixels(img, (x, y))

            set_pixels(result, (x, y), rgb)

    return result


img = cv2.imread('./data/L3.jpg')

res = affine_transformation(img, [(14, 14), (72, 464), (905, 681)])

cv2.imshow("Image", res)

cv2.waitKey(0)
