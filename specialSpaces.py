import cv2
import imutils
import numpy as np
from transformPiece import transformPiece
from readCSVFile import findSpecialInstructions


def checkSpecialSpaces(boardCorners):
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    ratio = frame.shape[0] / 800.0
    orig = frame.copy()
    frame = imutils.resize(frame, height=800)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, dictionary)

    if np.all(ids is not None):
        for x in range(len(ids)):
            ID = ids[x][0]
            topLeftX = corners[x][0][2][0]
            topLeftY = corners[x][0][2][1]
            bottomLeftX = corners[x][0][0][0]
            bottomLeftY = corners[x][0][0][1]
            center = (topLeftX + bottomLeftX) / 2, (topLeftY + bottomLeftY) / 2
            centerX = int(center[0])
            centerY = int(center[1])
            center = centerX, centerY
            center = transformPiece(center, boardCorners)
            if ID == 1:
                findSpecialInstructions(center)
