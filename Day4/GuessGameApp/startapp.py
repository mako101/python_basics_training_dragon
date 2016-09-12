import number as n
import game_logic, game_session, get_input, player_manager, counter

class StartApp(object):

    @staticmethod
    def start_game():

        # Load lives and scores from file
        # if either isn't found, use the default value(2nd arg)
        lives = counter.Counter.load_from_file('Lives', game_session.GameSession.DEFAULT_LIVES)
        score = counter.Counter.load_from_file('Score', game_session.GameSession.DEFAULT_SCORE)
        # generate the two numbers
        num = n.Number()
        
        first_number = num.gen_number()
        next_number = num.gen_number()

        print('Lives:', lives)
        print('Score:', score)
        print()
        print('The first number is', first_number)
        print("Do you think next number is higher or lower? ")

        # first we need to get users answer
        # we are also checking if they want to save and quit
        # hence we need to pass lives and score here
        user_answer = get_input.GetInput.user_choice()
        #print('User answer is', user_answer)

        # the gamelogic module decides whether the user won or lost
        outcome = game_logic.GameLogic.decide(first_number, next_number, user_answer)
        #print('The result is', result)

        # we pass the result to player manager class that will:
        # notify user
        # update lives count
        # update score count
        # call gameover module when user is out of lives
        pm = player_manager.PlayerManager(
            outcome=outcome,
            lives=lives,
            score=score,
            next_number=next_number,
            )
        pm.process_result()

        # reset the class instance to generate new numbers and call it again
        StartApp.start_game()

