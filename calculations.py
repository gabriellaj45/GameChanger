import math


def getShortestDistance(point, pointList):
    x1 = point[0]
    y1 = point[1]
    mini = 5000000
    saveIndex = 0
    for i in range(len(pointList)):
        for j in range(len(pointList[i])):
            x2 = pointList[i][0]
            y2 = pointList[i][1]
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            if distance < mini:
                saveIndex = i
                mini = distance
    return saveIndex
