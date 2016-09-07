# Import random number generator
from random import randint
from sys import exit

# lets generate a random 4-digit number
# We convert it to string to simplify comparison with user input
random_number = str(randint(1000,9999))

# Count the attempts it took the player to win
counter = 0

def startApp():

    print(random_number)

    # We don't care if they input letters so no need to check the input
    # as it won't break the application
    player_number=input('Please enter a 4 digit number: ')

    # this is the winning condition
    if player_number == random_number:
        print('Congratulations, you guessed the number!')
        print('You guessed the number in %d attempts' % counter)
        exit
    else:
        # Convert user's number into list,
        #  so that we can compare each character to the generated number
        player_chars = list(player_number)
        for character in player_chars:
            if character in random_number:
                print('You guessed', character)

    startApp()


startApp()
