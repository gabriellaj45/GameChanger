import cv2
import time
import numpy as np


def mouse_handler(event, x, y, flags, data):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(data['im'], (x, y), 1, (0, 0, 255), 2)
        cv2.imshow("Image", data['im'])
        # if len(data['points']) < 4:
        data['points'].append([x, y])
        print(x, y)


def get_four_points(im):
    # Set up data to send to mouse handler
    data = {}
    data['im'] = im.copy()
    data['points'] = []

    # Set the callback function for any mouse event
    cv2.imshow("Image", im)
    cv2.setMouseCallback("Image", mouse_handler, data)
    cv2.waitKey(0)
    points = np.vstack(data['points'])

    return points


# def getCorners():
if __name__ == '__main__':
    # Read in the image.
    im_src = cv2.imread("monopoly.jpg")

    # cap = cv2.VideoCapture(0)

    # _, im_src = cap.read()

    '''
        Click on the four corners of the book -- top left first and
        bottom left last -- and then hit ENTER
    '''
    # print("Click on the corners of the board in a clockwise order starting with the top left corner,"
         #  " then press ENTER")
    # Show image and wait for 4 clicks.
    im_src = cv2.resize(im_src, (800, 800))
    cv2.imshow("Image", im_src)
    pts_src = get_four_points(im_src)
    print(pts_src)

    # return pts_src
