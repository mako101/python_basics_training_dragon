import file_io
import life_counter
import gameover

class PlayerManager(object):

    # This does not work because trying to save refrence variable as an instant variable!!!

    ## DO NOT set other class instances as variables, just use them directly!!!

    def __init__(self, result, next_number):

        f = file_io.FileOps()
        no_of_lives = f.LoadFromFile

        # is it OK to use other class instances as attributes??
        # Needs to be a class variable?
        self.__lives = life_counter.LifeCounter(lives=no_of_lives)
        self.__result = result
        self.__next_number = next_number
        self.__gameover = gameover.GameOver()

    def showSecondNumber(self):
        print("The second number was:", self.__next_number)


    def showLives(self):
        print('Lives Remaining: ', self.__lives.displayLives(), '\n')

    def saveLifeCount(self):
        s = file_io.FileOps(data=self.__lives.displayLives())
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
            self.__gameover.askIfContinue()




