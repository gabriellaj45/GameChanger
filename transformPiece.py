import numpy as np
import cv2
from readCSVFile import findTileNum


def transformPiece(point, corners):
    pts_src = np.array(corners.corners)

    pts_dst = np.array([[0, 0], [800, 0], [800, 800], [0, 800]], dtype=float)

    # calculate matrix H
    h, status = cv2.findHomography(pts_src, pts_dst)
    a = np.array([point], dtype='float32')
    a = np.array([a])

    # finally, get the mapping
    pointsOut = cv2.perspectiveTransform(a, h)

    pointsOut = int(pointsOut[0][0][0]), int(pointsOut[0][0][1])
    # print(pointsOut)
    pointsOut = findTileNum(pointsOut)
    return pointsOut
