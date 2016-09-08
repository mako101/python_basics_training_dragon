import random

class NumberGenerator(object):

    def __init__(self):

        self.__firstNumber = random.randint(10, 100)
        self.__secondNumber = random.randint(10, 100)

    def getFirstNumber(self):

        return self.__firstNumber

    def getSecondNumber(self):

        return self.__secondNumber