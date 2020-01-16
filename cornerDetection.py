import cv2
from calculations import getShortestDistance
import numpy as np
import imutils
import math
from array import *
from boardRotate import rotateBoard


if __name__ == '__main__':
#def getBoardPoints(image):

    # For live stream
    # capturing video through webcam
    cap = cv2.VideoCapture(0)

    _, image = cap.read()

    # image = cv2.imread('Step3.jpg')

    ratio = image.shape[0] / 800.0
    orig = image.copy()
    image = imutils.resize(image, height=800)

    height = image.shape[0]
    width = image.shape[1]

    grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite('3.jpg', grayScale)
    #cv2.equalizeHist(grayScale, grayScale)
    #cv2.imwrite('4.jpg', grayScale)
    #grayScale = cv2.bilateralFilter(grayScale, 11, 17, 17) # do I need this?
    #cv2.imwrite('5.jpg', grayScale)
    _, thresh = cv2.threshold(grayScale, 105, 255, 0)
    #cv2.imwrite('6.jpg', thresh)
    cannyEdge = cv2.Canny(thresh, 125, 255)
    #cv2.imwrite('7.jpg', cannyEdge)


    # ones, and initialize our screen contour
    image2, contours, hierarchy = cv2.findContours(cannyEdge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # The board is the first element in the contours variable
    boardContour = contours.pop(0)
    # cv2.drawContours(image, [boardContour], 0, (0, 255, 0), 5)

    x = 0
    y = 0
    pointArray = []
    coordinateList = []
    '''
    rc = cv2.minAreaRect(boardContour)
    box = cv2.boxPoints(rc)
    for p in box:
        pt = (p[0], p[1])
        cv2.circle(image, pt, 10, (0, 0, 255), -1)
    '''
    for intLoopIndex in range(len(boardContour)):
        x, y = tuple(boardContour[intLoopIndex][0])
        pointArray.append((x, y))

    topLeft = getShortestDistance((0, 0), pointArray)
    topRight = getShortestDistance((width, 0), pointArray)
    bottomRight = getShortestDistance((width, height), pointArray)
    bottomLeft = getShortestDistance((0, height), pointArray)

    cv2.circle(image, pointArray[topLeft], 10, (0, 0, 255), -1)
    cv2.circle(image, pointArray[topRight], 10, (0, 0, 255), -1)
    cv2.circle(image, pointArray[bottomRight], 10, (0, 0, 255), -1)
    cv2.circle(image, pointArray[bottomLeft], 10, (0, 0, 255), -1)

    coordinateList.append(pointArray[topLeft])
    coordinateList.append(pointArray[topRight])
    coordinateList.append(pointArray[bottomRight])
    coordinateList.append(pointArray[bottomLeft])

    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gameBoard.jpg", image)
    # print(coordinateList)

    image = rotateBoard(coordinateList)
    #return image





