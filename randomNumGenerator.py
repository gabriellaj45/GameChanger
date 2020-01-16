import random
from readCSVFile import *


def getNum():
    numbers = getNumInfo()
    randomNum(random.randint(numbers["min"], numbers["max"]))
