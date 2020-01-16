import cv2
import numpy as np
from calculations import getShortestDistance
from corners import *
import imutils


def mouse_handler(event, x, y, flags, data):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(data['im'], (x, y), 1, (0, 0, 255), 2)
        cv2.imshow("Image", data['im'])
        if len(data['points']) < 4:
            data['points'].append((x, y))


def get_four_points(im):
    # Set up data to send to mouse handler
    data = {}
    data['im'] = im.copy()
    data['points'] = []

    # Set the callback function for any mouse event
    # im = cv2.resize(im, (750, 700))
    # cv2.imshow("ThisImage", im)
    cv2.setMouseCallback("Image", mouse_handler, data)
    cv2.waitKey(0)

    # Convert array to np.array
    # points = np.vstack(data['points']).astype(float)
    points = data['points']

    return points


def clickCorners():

    cap = cv2.VideoCapture(0)

    _, im_src = cap.read()

    ratio = im_src.shape[0] / 800.0
    orig = im_src.copy()
    image = imutils.resize(im_src, height=800)

    # Show image and wait for 4 clicks.
    cv2.imshow("Image", image)
    pts_src = get_four_points(image)

    return pts_src


def verifyCorners():
    while True:
        cap = cv2.VideoCapture(0)
        _, image = cap.read()

        ratio = image.shape[0] / 800.0
        orig = image.copy()
        image = imutils.resize(image, height=800)

        height = image.shape[0]
        width = image.shape[1]

        grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(grayScale, 105, 255, 0)

        cannyEdge = cv2.Canny(thresh, 125, 255)

        # ones, and initialize our screen contour
        image2, contours, hierarchy = cv2.findContours(cannyEdge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)

        # The board is the first element in the contours variable
        boardContour = contours.pop(0)

        x = 0
        y = 0
        pointArray = []
        coordinateList = []

        for intLoopIndex in range(len(boardContour)):
            x, y = tuple(boardContour[intLoopIndex][0])
            pointArray.append((x, y))

        topLeft = getShortestDistance((0, 0), pointArray)
        topRight = getShortestDistance((width, 0), pointArray)
        bottomRight = getShortestDistance((width, height), pointArray)
        bottomLeft = getShortestDistance((0, height), pointArray)

        cv2.circle(image, pointArray[topLeft], 5, (0, 0, 255), -1)
        cv2.circle(image, pointArray[topRight], 5, (0, 0, 255), -1)
        cv2.circle(image, pointArray[bottomRight], 5, (0, 0, 255), -1)
        cv2.circle(image, pointArray[bottomLeft], 5, (0, 0, 255), -1)

        coordinateList.append(pointArray[topLeft])
        coordinateList.append(pointArray[topRight])
        coordinateList.append(pointArray[bottomRight])
        coordinateList.append(pointArray[bottomLeft])

        print("Enter 1 if yes, 2 if you want to manually select the corners, and 0 if no")

        image = cv2.resize(image, (750, 700))
        cv2.imshow("Game Board with Corners Detected", image)
        cv2.waitKey(40) & 0xFF

        key = input()

        if key == '0':
            print('corners not properly detected')
            cv2.destroyAllWindows()
            continue
        if key == '1':
            corners = Corners()
            corners.setCorners(coordinateList)
            # print(corners.getCorners())
            cv2.destroyAllWindows()
            return corners

        if key == '2':
            cv2.destroyAllWindows()
            print("Click the corners of the board in clockwise order starting at the top left")
            boardCorners = clickCorners()
            corners = Corners()
            corners.setCorners(boardCorners)
            # print(corners.getCorners())
            cv2.destroyAllWindows()
            return corners






