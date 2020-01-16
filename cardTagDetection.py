import numpy as np
import cv2
import cv2.aruco as aruco
import imutils
from readCSVFile import readCard
from audioFeedback import *


def getCard():
    idList = []

    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    ratio = frame.shape[0] / 800.0
    orig = frame.copy()
    frame = imutils.resize(frame, height=800)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # res = cv2.aruco.detectMarkers(gray, dictionary)
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, dictionary)

    if np.all(ids is not None):
        for x in range(len(ids)):
                ID = ids[x][0]
                idList.append(ID)
                if ID >= 11 and ID <= 40:
                    cardID = ID
                    readCard(cardID)
                    return
    tryAgain()
