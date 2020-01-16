from os import system


def introduction():

    system('say -v Samantha Welcome to Game Changer')
    system('say -v Samantha Press 1 to hear instructions for using this system')
    system('say -v Samantha Or press 0 to continue to the game')

    while True:
        key = input(' ')
        if key == '1':
            instructions()
            system('say -v Samantha Press 1 if you want the keys for the game repeated')
            system('say -v Samantha Or press 0 to continue to the game')
        if key == '0':
            return


def begin():
    system('say -v Samantha You may begin the game')


def instructions():

    system('say -v Samantha Press 1 to get the locations of your game pieces')
    system('say -v Samantha Press 2 to get the locations of your opponent game pieces')
    system('say -v Samantha Press 3 to get the locations of all game pieces')
    system('say -v Samantha Press 4 to read the information on the card')
    system('say -v Samantha Press 5 to get the instructions for using the system during the game')
    system('say -v Samantha Press 6 to get information about your money')
    system('say -v Samantha Press 7 followed by 1 for property info 2 for house location 3 for hotel location')
    system('say -v Samantha Press 0 to quit the game at any time')


def userPieceLocation(tileNum):
    if tileNum is None:
        return
    speak = 'say -v Samantha ' + tileNum
    system('say -v Samantha Your piece is at ')
    system(speak)


def oppPieceLocation(tileNum):
    if tileNum is None:
        return
    speak = 'say -v Samantha ' + tileNum
    system('say -v Samantha Your opponents piece is at ')
    system(speak)


def cardInformation(desc):
    if desc is None:
        return
    speak = 'say -v Samantha ' + desc
    system(speak)


def tryAgain():
    system('say -v Samantha Sorry, no cards were detected. Please try again')


def specialSpace(info):
    speak = 'say -v Samantha ' + info
    system(speak)


def randomNum(info):
    speak = 'say -v Samantha ' + str(info)
    system(speak)


def showMeTheMoney(money, amount):
    speak = 'say -v Samantha ' + str(money) + str(amount)
    system(speak)


def propertyPrompt(name):
    speak = 'say -v Samantha Press 0 if you want information about ' + name + \
            '... 1 if you are looking for a different property... ' \
                '2 when you are finished getting information'
    system(speak)


def houseInformation(tileNum):
    if tileNum is None:
        return
    speak = 'say -v Samantha ' + tileNum
    system('say -v Samantha There is a house at ')
    system(speak)


def hotelInformation(tileNum):
    if tileNum is None:
        return
    speak = 'say -v Samantha ' + tileNum
    system('say -v Samantha There is a hotel at ')
    system(speak)


def noHomes():
    system('say -v Samantha There are no houses on the board')


def noHotels():
    system('say -v Samantha There are no hotels on the board')


def sayPropertyInfo(desc, info):
    speak = 'say -v Samantha ' + desc + ' ' + info
    system(speak)


def gameOver():
    system('say -v Samantha Game over...')
