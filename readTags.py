import numpy as np
import cv2
#from cardDetection import getCard
import imutils


#def findTags(numCheck):
if __name__ == '__main__':
    numCheck = 2
    cap = cv2.VideoCapture(0)
    #dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    #dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)

    #while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    ratio = frame.shape[0] / 700.0
    orig = frame.copy()
    frame = imutils.resize(frame, height=700)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # res = cv2.aruco.detectMarkers(gray, dictionary)
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, dictionary)

    if np.all(ids is not None):
        myPieceList = []
        gamePieceList = []
        cv2.aruco.drawDetectedMarkers(frame, corners)
        if numCheck == 0:
            for x in range(len(ids)):
                ID = ids[x][0]
                if ID <= 6:
                    topLeftX = corners[x][0][2][0]
                    topLeftY = corners[x][0][2][1]
                    bottomLeftX = corners[x][0][0][0]
                    bottomLeftY = corners[x][0][0][1]
                    center = (topLeftX + bottomLeftX) / 2, (topLeftY + bottomLeftY) / 2
                    gamePieceList.append(center)
                    print(gamePieceList)
            # return gamePieceList
            # cv2.circle(frame, (topLeftX, topLeftY), 5, (0, 0, 255), -1)
            # cv2.circle(frame, (bottomLeftX, bottomLeftY), 5, (0, 0, 255), -1)
            # center = (topLeftX + bottomLeftX) / 2, (topLeftY + bottomLeftY) / 2
            # centerX = int(center[0])
            # centerY = int(center[1])
            # cv2.circle(frame, (centerX, centerY), 5, (0, 0, 255), -1)
            # cv2.aruco.drawDetectedMarkers(frame, center)
            # print('Pieces')
        elif numCheck == 1:
            for x in range(len(ids)):
                ID = ids[x][0]
                if ID <= 3:
                    topLeftX = corners[x][0][2][0]
                    topLeftY = corners[x][0][2][1]
                    bottomLeftX = corners[x][0][0][0]
                    bottomLeftY = corners[x][0][0][1]
                    center = (topLeftX + bottomLeftX) / 2, (topLeftY + bottomLeftY) / 2
                    centerX = int(center[0])
                    centerY = int(center[1])
                    center = centerX, centerY
                    myPieceList.append(center)
                    print(myPieceList)
            # return myPieceList
        elif numCheck == 2:
            # make a check for no cards being found or visible
            idList = []
            for x in range(len(ids)):
                ID = ids[x][0]
                idList.append(ID)
                if ID >= 39:
                    cardID = ID
                    # getCard(cardID)
                    # break


        # Display the resulting frame
        cv2.imwrite('GameDetection.jpg', frame)
        '''
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        '''
    '''
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    '''

