import csv
from audioFeedback import *


def findTileNum(points):
    xCoor, yCoor = points
    with open('MonopolyInfo.csv') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        for row in csvReader:
            if lineCount < 2:
                lineCount += 1
                continue
            else:
                tileNumber = row[0]
                xStartCoor = int(row[1])
                xEndCoor = int(row[2])
                yStartCoor = int(row[3])
                yEndCoor = int(row[4])

                if xCoor >= xStartCoor:
                    if xCoor <= xEndCoor:
                        if yCoor >= yStartCoor:
                            if yCoor <= yEndCoor:
                                return tileNumber


def readCard(number):
    with open('MonopolyCardDescriptions.csv') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=",")
        lineCount = 0
        if number is None:
            print('No card')
        for row in csvReader:
            if lineCount == 0:
                lineCount += 1
                continue
            else:
                num = int(row[0])
                description = row[1]
                if num == number:
                    # print(description)
                    cardInformation(description)
                    break


def getNumInfo():
    with open('MonopolyInfo.csv') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        for row in csvReader:
            if lineCount == 0:
                minNum = int(row[1])
                maxNum = int(row[3])
                numbers = {"min": minNum, "max": maxNum}
                break
    return numbers


def findSpecialInstructions(spaceNum):
    with open('MonopolyInfo.csv') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        for row in csvReader:
            if lineCount < 2:
                lineCount += 1
                continue
            else:
                theSpaceNum = row[0]
                specialInfo = row[5]
                if spaceNum == theSpaceNum:
                    if specialInfo:
                        specialSpace(specialInfo)
                        return


def propertyInfo():
    theProperties = []
    with open('MonopolyProperties.csv') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        for row in csvReader:
            if lineCount == 0:
                lineCount += 1
                continue
            propertyName = row[0]
            rent = row[1]
            oneHouse = row[2]
            twoHouse = row[3]
            threeHouse = row[4]
            fourHouse = row[5]
            hotel = row[6]
            mortgage = row[7]
            houseCost = row[8]
            hotelCost = row[9]
            theProperty = {"name": propertyName, "rent": rent, "1 house": oneHouse, "2 houses": twoHouse,
                        "3 houses": threeHouse, "4 houses": fourHouse, "hotel": hotel, "mortgage value": mortgage,
                        "house cost": houseCost, "hotel cost": hotelCost}
            theProperties.append(theProperty)
            propertyPrompt(propertyName)
            key = input()
            if key == '1':
                continue
            if key == '0':
                for x, y in theProperty.items():
                    sayPropertyInfo(x, y)
            if key == '2':
                break


if __name__ == '__main__':
    # findTileNum((360, 45))
    # readCard(45)
    # findSpecialInstructions(2)
    propertyInfo()
