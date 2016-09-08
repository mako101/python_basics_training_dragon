import gamestart, gamelife

#display welcome message
print("Welcome to the Guess Game App")
print("I will ask you to guess if an hidden number is higher or lower than thw number displayed on screen")

#set the life
gamelife.GameLife.setLifeFromFile()

#start the game
gamestart.GameStart.startGame()
#I did not create an instance of gamestart class to access the method startGame because the method is static method