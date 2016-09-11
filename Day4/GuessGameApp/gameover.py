
class GameOver(object):

    @staticmethod
    def askIfContinue():

        print('You do not have any more lives, do you wish to continue?')
        user_input = input('Press Y to continue or any other key to exit')

        if user_input != 'Y' and user_input != 'y':
            print('Goodbye')
            exit()

