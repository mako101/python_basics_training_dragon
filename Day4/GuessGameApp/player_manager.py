import X_file_io
import X_lifecounter
import gameover

class PlayerManager(object):

    def __init__(self, result, next_number):

        f = X_file_io.FileOps()
        no_of_lives = f.LoadFromFile

        # is it OK to use other class instances as attributes??
        self.__lives = X_lifecounter.LifeCounter(lives=no_of_lives)
        self.__result = result
        self.__next_number = next_number


    def showSecondNumber(self):
        print("The second number was:", self.__next_number)


    def showLives(self):
        print('Lives Remaining: ', self.__lives.displayLives(), '\n')

    def saveLifeCount(self):
        s = X_file_io.FileOps(data=self.__lives.displayLives())
        s.SaveToFile()

    def processResult(self):

        if self.__result == 1:
            print('You Win!')
            self.showSecondNumber()
            self.__lives.addLife()
            self.showLives()
            self.saveLifeCount()

        elif self.__result == 0:
            print('You Lost')
            self.showSecondNumber()
            self.__lives.loseLife()
            self.showLives()
            self.saveLifeCount()

        if self.__lives.displayLives() == 0:
            # reset the life count and call the gameover class
            self.__lives.resetLives()
            self.saveLifeCount()
            gameover.GameOver.askIfContinue()





