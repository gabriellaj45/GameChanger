import cv2
import numpy as np
from corners import *
import imutils


def rotateBoard(coorList):
    im_src = cv2.imread('gameboard.jpg')
    # im_src = image

    ratio = im_src.shape[0] / 800.0
    orig = im_src.copy()
    im_src = imutils.resize(im_src, height=800)

    # Destination image
    size = (800, 800)

    im_dst = np.zeros(size, np.uint8)

    pts_dst = np.array(
        [
            [0, 0],
            [800, 0],
            [800, 800],
            [0, 800]
        ], dtype=float
    )

    # im_src = cv2.resize(im_src, (700, 700))
    # cv2.imshow("Image", im_src)
    pts_src = np.array(coorList)

    print(pts_src)

    # Calculate the homography
    h, status = cv2.findHomography(pts_src, pts_dst)

    # Warp source image to destination
    im_dst = cv2.warpPerspective(im_src, h, size[0:2])

    # Show output
    cv2.imwrite("rotatedBoard.jpg", im_dst)
    return im_dst


'''
def transformBoard(image):
    im_src = image

    # Destination image
    size = (800, 800)

    im_dst = np.zeros(size, np.uint8)

    pts_dst = np.array(
        [
            [0, 0],
            [size[0], 0],
            [size[0], size[1]],
            [0, size[1]]
        ], dtype=float
    )

    pts_src = np.array(
        [
            [449, 92],
            [1070, 103],
            [1163, 736],
            [370, 723]
        ], dtype=float
    )

    print(pts_src)

    # Calculate the homography
    h, status = cv2.findHomography(pts_src, pts_dst)

    # Warp source image to destination
    im_dst = cv2.warpPerspective(im_src, h, size[0:2])

    # Show output
    cv2.imwrite("gameBoard.jpg", im_dst)
    cv2.imwrite('tester.jpg', im_dst)
    return im_dst
'''