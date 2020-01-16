from audioFeedback import *
from cardTagDetection import getCard
from pieceTagDetection import *
from verifyCorners import verifyCorners
from specialSpaces import checkSpecialSpaces
from randomNumGenerator import getNum
from readCSVFile import propertyInfo


def startGame(corners):
    begin()
    boardCorners = corners
    while True:
        key = input()
        if key == '9':
            checkSpecialSpaces(boardCorners)
        if key == '4':
            getCard()
        if key == '3':
            myPieceList = getPieces(0, boardCorners)
            for piece in myPieceList:
                userPieceLocation(piece)
            myPieceList = getPieces(2, boardCorners)
            for piece in myPieceList:
                oppPieceLocation(piece)
        if key == '1':
            # system user's pieces
            myPieceList = getPieces(0, boardCorners)
            for piece in myPieceList:
                userPieceLocation(piece)
        if key == '2':
            # opponent's pieces
            myPieceList = getPieces(2, boardCorners)
            for piece in myPieceList:
                oppPieceLocation(piece)
        if key == '5':
            instructions()
        if key == '6':
            yourMoney = getMoney()
            for money, amount in yourMoney.items():
                showMeTheMoney(money, amount)
        if key == '7':
            next = input()
            if next == '1':
                propertyInfo()
            if next == '2':
                homes = getHomesHotels(0, boardCorners)
                if homes:
                    for house in homes:
                        houseInformation(house)
                else:
                    noHomes()
            if next == '3':
                hotels = getHomesHotels(1, boardCorners)
                if hotels:
                    for hotel in hotels:
                        hotelInformation(hotel)
                else:
                    noHotels()
        if key == '99':
            # board has shifted need to get the new corners
            boardCorners = verifyCorners()
        if key == '0':
            gameOver()
            exit(0)
        if key == '':
            getNum()


