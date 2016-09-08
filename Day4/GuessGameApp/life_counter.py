
class LifeCounter(object):

    def __init__(self, lives = 3, reset_counter = 3):

        self.__lives = lives
        self.__reset_counter = reset_counter

    def displayLives(self):
        return self.__lives

    def addLife(self):
        self.__lives += 1

    def loseLife(self):
        self.__lives -= 1

    def resetLives(self):
        self.__lives = self.__reset_counter
