import number as n
import game_logic, compare_numbers, get_input, player_manager, file_io


class StartApp(object):
        

    @staticmethod
    def startGame():
        

        # Read current lives from settings file
        current_lives = file_io.FileOps.LoadFromFile()

        # generate the two numbers
        num = n.Number()
        
        first_number = num.gen_number()
        next_number = num.gen_number()

        print('Lives:', current_lives)
        print('The first number is', first_number)

        # first we need to get users answer
        gi = get_input.GetInput(first_number)
        user_answer = gi.get_input()
        #print('User answer is', user_answer)

        # then the application compares two generated numbers and stores the result
        cn = compare_numbers.CompareNumbers(first_number, next_number)
        app_answer = cn.compare()
        #print('App answer is', app_answer)

        # Now we compare user's answer to app's answer and decide if there is a match
        gl = game_logic.GameLogic(app_answer, user_answer)
        result = gl.decide()
        #print('The result is', result)

        # we pass the match to the pm module that determines if the player has won or lost and manages lives
        pm = player_manager.PlayerManager(result=result, next_number=next_number)
        pm.processResult()

        # reset the class instance to generate new numbers and call it again
        StartApp.startGame()

