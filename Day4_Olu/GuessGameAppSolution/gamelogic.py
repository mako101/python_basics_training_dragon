import gamelife as gl

class GameLogic(object):

    __WINSTATEMENT = "You win"
    __LOSESTATEMENT = "You lose"
    __INVALIDSTATEMENT = "Invalid response, please type H for Higher and L for Lower"

    def getPoints(self, userGuess, firstNumber, secondNumber):

        #change user guess to uppercase
        userGuess = str.upper(userGuess) #or str(userGuess).upper()

        #logic
        if userGuess == "H":

            if secondNumber > firstNumber:

                #increase life
                gl.GameLife.increaseLife()

                #display you win
                return GameLogic.__WINSTATEMENT

            else:

                #decrease life
                gl.GameLife.decreaseLife()

                #display you lose
                return GameLogic.__LOSESTATEMENT

        elif userGuess == "L":

            if secondNumber < firstNumber:

                #increase life
                gl.GameLife.increaseLife()

                #display you win
                return GameLogic.__WINSTATEMENT

            else:

                #decrease life
                gl.GameLife.decreaseLife()

                #display you lose
                return GameLogic.__LOSESTATEMENT

        else:

            return GameLogic.__INVALIDSTATEMENT