from gamePlay import *
from audioFeedback import *
from verifyCorners import verifyCorners


if __name__ == '__main__':
    while True:
        # system("say -v Samantha Are the corners of the board correctly detected in the image?")
        print('Are the corners of the board correctly detected in the image?')
        corners = verifyCorners()

        introduction()

        startGame(corners)
