import number as n
import game_logic, compare_numbers, get_input, player_manager, file_io

# Can I leave this outside the start app?
print('Weclome to the Guess Game App!', '\n')

class StartApp(object):

    def __init__(self):
        # generate the two numbers
        num = n.Number()

        # Read current lives from settings file
        f = file_io.FileOps()

        self.current_lives = f.LoadFromFile()
        self.__first_number = num.gen_number()
        self.__next_number = num.gen_number()

    def startGame(self):

        print('Lives:', self.current_lives)
        print('The first number is', self.__first_number)

        # first we need to get users answer
        gi = get_input.GetInput(self.__first_number)
        user_answer = gi.get_input()
        #print('User answer is', user_answer)

        # then the application compares two generated numbers and stores the result
        cn = compare_numbers.CompareNumbers(self.__first_number, self.__next_number)
        app_answer = cn.compare()
        #print('App answer is', app_answer)

        # Now we compare user's answer to app's answer and decide if there is a match
        gl = game_logic.GameLogic(app_answer, user_answer)
        result = gl.decide()
        #print('The result is', result)

        # we pass the match to the pm module that determines if the player has won or lost and manages lives
        pm = player_manager.PlayerManager(result=result, next_number=self.__next_number)
        pm.processResult()

        # reset the class instance to generate new numbers and call it again
        st = StartApp()
        st.startGame()


st = StartApp()

st.startGame()

# TO DO

# run continuously with new numbers every time
# have the lives remaining in the bottom + show lives before the user guess
# Add restart
