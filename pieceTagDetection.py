import numpy as np
import cv2
import cv2.aruco as aruco
import imutils
from transformPiece import transformPiece


def getPieces(code, boardCorners):
    myPieceList = []
    gamePieceList = []
    oppPieceList = []

    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    ratio = frame.shape[0] / 800.0
    orig = frame.copy()
    frame = imutils.resize(frame, height=800)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, dictionary)

    if np.all(ids is not None):
        if code == 0:
            for x in range(len(ids)):
                ID = ids[x][0]
                if ID == 1:
                    topLeftX = corners[x][0][2][0]
                    topLeftY = corners[x][0][2][1]
                    bottomLeftX = corners[x][0][0][0]
                    bottomLeftY = corners[x][0][0][1]
                    center = (topLeftX + bottomLeftX) / 2, (topLeftY + bottomLeftY) / 2
                    centerX = int(center[0])
                    centerY = int(center[1])
                    center = centerX, centerY
                    center = transformPiece(center, boardCorners)
                    myPieceList.append(center)
            return myPieceList
        elif code == 1:
            for x in range(len(ids)):
                ID = ids[x][0]
                if ID <= 8:
                    topLeftX = corners[x][0][2][0]
                    topLeftY = corners[x][0][2][1]
                    bottomLeftX = corners[x][0][0][0]
                    bottomLeftY = corners[x][0][0][1]
                    center = (topLeftX + bottomLeftX) / 2, (topLeftY + bottomLeftY) / 2
                    centerX = int(center[0])
                    centerY = int(center[1])
                    center = centerX, centerY
                    center = transformPiece(center, boardCorners)
                    gamePieceList.append(center)
            return gamePieceList
        elif code == 2:
            for x in range(len(ids)):
                ID = ids[x][0]
                if ID >= 2 and ID <= 8:
                    topLeftX = corners[x][0][2][0]
                    topLeftY = corners[x][0][2][1]
                    bottomLeftX = corners[x][0][0][0]
                    bottomLeftY = corners[x][0][0][1]
                    center = (topLeftX + bottomLeftX) / 2, (topLeftY + bottomLeftY) / 2
                    centerX = int(center[0])
                    centerY = int(center[1])
                    center = centerX, centerY
                    center = transformPiece(center, boardCorners)
                    oppPieceList.append(center)
            return oppPieceList


def getMoney():
    numOnes = 0
    numFives = 0
    numTens = 0
    numTwenty = 0
    numFifty = 0
    numHundred = 0
    numFiveHundred = 0
    money = {"ones": 0, "fives": 0, "tens": 0, "twenties": 0, "hundreds": 0, "five hundreds": 0}

    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    ratio = frame.shape[0] / 800.0
    orig = frame.copy()
    frame = imutils.resize(frame, height=800)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, dictionary)

    if np.all(ids is not None):
        for x in range(len(ids)):
            ID = ids[x][0]
            if ID == 41:
                numOnes = numOnes + 1
            if ID == 42:
                numFives = numFives + 1
            if ID == 43:
                numTens = numTens + 1
            if ID == 44:
                numTwenty = numTwenty + 1
            if ID == 45:
                numFifty = numFifty + 1
            if ID == 46:
                numHundred = numHundred + 1
            if ID == 47:
                numFiveHundred = numFiveHundred + 1
    money["ones"] = numOnes
    money["fives"] = numFives
    money["tens"] = numTens
    money["twenties"] = numTwenty
    money["hundreds"] = numHundred
    money["five hundreds"] = numFiveHundred
    return money


def getHomesHotels(code, boardCorners):
    houseList = []
    hotelList = []

    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    ratio = frame.shape[0] / 800.0
    orig = frame.copy()
    frame = imutils.resize(frame, height=800)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, dictionary)

    if np.all(ids is not None):
        if code == 0:  # houses
            for x in range(len(ids)):
                ID = ids[x][0]
                if ID == 9:
                    topLeftX = corners[x][0][2][0]
                    topLeftY = corners[x][0][2][1]
                    bottomLeftX = corners[x][0][0][0]
                    bottomLeftY = corners[x][0][0][1]
                    center = (topLeftX + bottomLeftX) / 2, (topLeftY + bottomLeftY) / 2
                    centerX = int(center[0])
                    centerY = int(center[1])
                    center = centerX, centerY
                    center = transformPiece(center, boardCorners)
                    houseList.append(center)
            return houseList
        elif code == 1:  # hotels
            for x in range(len(ids)):
                ID = ids[x][0]
                if ID == 10:
                    topLeftX = corners[x][0][2][0]
                    topLeftY = corners[x][0][2][1]
                    bottomLeftX = corners[x][0][0][0]
                    bottomLeftY = corners[x][0][0][1]
                    center = (topLeftX + bottomLeftX) / 2, (topLeftY + bottomLeftY) / 2
                    centerX = int(center[0])
                    centerY = int(center[1])
                    center = centerX, centerY
                    center = transformPiece(center, boardCorners)
                    hotelList.append(center)
            return hotelList