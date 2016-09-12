import configmanager as c
import startapp


class GameSession(object):

    DEFAULT_LIVES = 3
    DEFAULT_SCORE = 0


    @staticmethod
    def reset_config():
        # reset lives and score
        c.FileOps.save_value('Lives', GameSession.DEFAULT_LIVES)
        c.FileOps.save_value('Score', GameSession.DEFAULT_SCORE)

    @staticmethod
    def new_game():
        print('\nYou will restart with 3 lives and a score of 0. Are you sure?')
        user_input = input('Press Y to confirm or any other to cancel')

        if user_input == 'Y' or user_input == 'y':

            GameSession.reset_config()

        startapp.StartApp.start_game()

    @staticmethod
    def game_over():

        GameSession.reset_config()

        print('\nYou do not have any more lives, do you wish to restart the game?')
        user_input = input('Press Y to continue or any other key to exit')

        if user_input != 'Y' and user_input != 'y':
            print('Goodbye')
            exit()

    @staticmethod
    def save_and_quit():
        print('\nYour lives and score will be saved')
        print('Goodbye!')
        # c.Counter.save_to_file('Lives', lives)
        # c.Counter.save_to_file('Score', score)
        exit()

