#Question
#Generate a random four digit number
#The player has to keep inputting four digit numbers until they guess the randomly generated number
#After each unsuccessful try, it should say how many numbers they got correct but not which position they got right
#At the end of the game, it should congratulate the user and say how many tries it took

#Solution
import random

# print(random.randint(1000, 9999))

#try variable equal to 1 - this is the first try
tries = 1

def startApp(random4DigitNumber):

    global tries

    #ask user to guess the 4 digit number you generated above
    userGuess = input("Can you guess the 4 digit number I have?")

    #check if user's guess is the same as the 4 digit random number
    if userGuess == random4DigitNumber:

        #if yes, say user guess correctly
        print("Congratulations, you got this right with %s attempt(s)" %tries)

        return #stop

    #check if the length of the response is 4 character
    elif len(userGuess) != 4:

        print("Please enter a four digit number!!!")

        #add line space
        print()

        #repeat recursion by calling method
        startApp(random4DigitNumber)

    else:

        #this is a 4 digit number, check how many guess is correct
        positionsGuessedCorrectly = 0

        #check first position
        if userGuess[0] == random4DigitNumber[0]:

            #increment
            positionsGuessedCorrectly += 1

        #check second position
        if userGuess[1] == random4DigitNumber[1]:

            #increment
            positionsGuessedCorrectly += 1

        #check third position
        if userGuess[2] == random4DigitNumber[2]:

            #increment
            positionsGuessedCorrectly += 1

        #check fourth position
        if userGuess[3] == random4DigitNumber[3]:

            #increment
            positionsGuessedCorrectly += 1

        #display result
        print("You guessed wrongly and got %s digits correct and have %d attempt(s)" %(positionsGuessedCorrectly, tries))

        #increment tries
        tries += 1

        #add line space
        print()

        #repeat
        startApp(random4DigitNumber)



#generate a random 4 character number
random4DigitNumber = str(random.randint(1000, 9999))

#start the exercise
startApp(random4DigitNumber)