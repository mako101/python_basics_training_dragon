import numbergenerator as ng
import gamelogic as gl
import gamelife

class GameStart(object):

    #method below is static, notice no self parameter
    @staticmethod
    def startGame():

        #display life
        print("Life:", gamelife.GameLife.getLife())

        #check if user have a life or not
        if gamelife.GameLife.getLife() < 1:

            #no life
            print("You do not have any more life, do you wish to restart or quit?")
            print("(Type R to restart or any key to quit)")

            #save response
            userResponse = str(input()).upper()

            if (userResponse == "R"):

                #restart
                gamelife.GameLife.resetLife()

                #line space
                print()

                #call the method
                GameStart.startGame()

            else:

                #quit
                print("Thank you for playing, bye!!!")

        else:

            #create an instance of number generator
            numGen = ng.NumberGenerator()

            print("Here is a number:", numGen.getFirstNumber())

            #display
            print("Do you think the next number I will display will be higher or lower?")
            print("(Type H for Higher and L for Lower)")

            #save user response
            userResponse = input()

            #create an instance of gamelogic
            gLogic = gl.GameLogic()

            #display result
            print(gLogic.getPoints(userGuess=userResponse, firstNumber=numGen.getFirstNumber(), secondNumber=numGen.getSecondNumber()))

            #display the next number
            print("The next number was", numGen.getSecondNumber())

            #save life
            gamelife.GameLife.saveLifeToFile()

            #add line space
            print()

            #repeat process by recursion
            GameStart.startGame()