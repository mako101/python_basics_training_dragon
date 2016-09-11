import startapp
import counter

print('Welcome to the Guess Game App!', '\n')

# Load lives and scores from file
# if either isn't found, use the default value(2nd arg)
lives = counter.Counter.loadFromFile('Lives', 3)
score = counter.Counter.loadFromFile('Score', 0)

# Start the game
startapp.StartApp.startGame(lives, score)

# TO DO

# have the lives remaining in the bottom + show lives before the user guess
# Add restart
# Add scores! Lose them if you run out of lives

# -  turn lifecounter class iot counter that can be used to count both lives and scores, and save different results into file

#  separate instances of the counter class or lives and points


# Read config settings from file

# - turn data from file into a discitionary - if feasible!