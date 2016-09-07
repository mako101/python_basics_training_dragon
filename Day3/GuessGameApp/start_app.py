import number as n
import game_logic, compare_numbers, get_input, player_manager

# # generate the two numbers
# num = n.Number()
# first_number = num.gen_number()
# next_number = num.gen_number()

class StartApp(object):

    def __init__(self):
        # generate the two numbers
        num = n.Number()

        self.__first_number = num.gen_number()
        self.__next_number = num.gen_number()

    def startGame(self):

        print('The first number is', self.__first_number)

        # first we need to get users answer
        gi = get_input.GetInput(self.__first_number)
        user_answer = gi.get_input()
        print(user_answer)

        # then the application compares two generated numbers and stores the result
        cn = compare_numbers.CompareNumbers(self.__first_number, self.__next_number)
        app_answer = cn.compare()
        #print(app_answer)

        # Now we compare user's answer to app's answer and decide if there is a match
        gl = game_logic.GameLogic(app_answer, user_answer)
        result = gl.decide()

        # we pass the match to the pm module that determines if the player has won or lost and manages lives
        pm = player_manager.PlayerManager(result)
        pm.processResult()

        print("The second number was:", self.__next_number)


        self.startGame()


st = StartApp()

st.startGame()

# TO DO

# run continuously with new numbers every time
# have the lives remaining in the bottom + show lives before the user guess
# Add restart
