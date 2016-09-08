
class GameOver(object):

    def __init__(self):
        pass

    def askIfContinue(self):

        print('You do not have any more lives, do you wish to continue?')
        user_input = input('Press Y to continue or any other key to exit')

        if user_input != 'Y' or user_input != 'y':
            print('Goodbye')
            exit()