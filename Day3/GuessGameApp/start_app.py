import number as n
import game_logic, compare_numbers, get_input


class StartApp(object):

    def __init__(self):

        # we generate numbers first
        num = n.Number()

        self.__first_number = num.gen_number()
        self.__next_number = num.gen_number()


    def startGame(self):

        # first we need to get users answer
        gi = get_input.GetInput(self.__first_number)
        user_answer = gi.get_input()
        #print(user_answer)

        # then the application compares two generated numbers and stores the result
        cn = compare_numbers.CompareNumbers(self.__first_number, self.__next_number)
        app_answer = cn.compare()
        #print(app_answer)

        # Now we compare user's answer to app's answer and decide if the user won or lost
        gl = game_logic.Game_Logic(app_answer, user_answer)
        outcome = gl.decide()

        print(outcome)

        print("The second number was:", self.__next_number)





st = StartApp()

st.startGame()


