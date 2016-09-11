import X_file_io

class LifeCounter(object):
    
    # We set up the default amount of lives and set the lives to it if there not found in the file
    __DEFAULT_LIVES = 3

    # This is class variable, so it will be updated everywhere throughout the course of the game
    __LIVES = __DEFAULT_LIVES

    @staticmethod
    def displayLives():
        return LifeCounter.__LIVES

    @staticmethod
    def addLife():
        LifeCounter.__LIVES += 1

    @staticmethod
    def loseLife():
        LifeCounter.__LIVES -= 1

    @staticmethod
    def resetLives():
        LifeCounter.__LIVES = LifeCounter.__DEFAULT_LIVES

    @staticmethod
    def saveLivesToFile():
        X_file_io.FileOps.SaveToFile('Lives:' + str(LifeCounter.__LIVES))

    @staticmethod
    def loadLivesFromFile():

        # we dont do anything here if exception is caught
        # This is so that the game can start without the settings file
        try:
            saved = X_file_io.FileOps.LoadFromFile().split(':')[1]
            saved = int(saved)
            print(saved)
            LifeCounter.__LIVES = saved
        except Exception as e:
            print(e)
            '''do nothing'''

LifeCounter.loadLivesFromFile()