import cv2  # import the OpenCV library
import numpy as np  # import the numpy library
import keyboard  # using module keyboard
'''
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('4'):  # if key 'q' is pressed
            print('You Pressed A Key!')
            break  # finishing the loop
        else:
            pass
    except:
        break
'''
if __name__ == '__main__':

    # provide points from image 1
    pts_src = np.array([[222, 39], [586, 38], [632, 683], [186, 681]])
    # corresponding points from image 2 (i.e. (154, 174) matches (212, 80))
    pts_dst = np.array([[0, 0], [800, 0], [800, 800], [0, 800]])

    # calculate matrix H
    h, status = cv2.findHomography(pts_src, pts_dst)

    # provide a point you wish to map from image 1 to image 2
    a = np.array([[400, 679]], dtype='float32')
    a = np.array([a])

    # finally, get the mapping
    pointsOut = cv2.perspectiveTransform(a, h)
    print(pointsOut)