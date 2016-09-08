
class GameOver(object):

    # you dont have to use constructor if you dont want to!

    def askIfContinue(self):

        print('You do not have any more lives, do you wish to continue?')
        user_input = input('Press Y to continue or any other key to exit')

        if user_input != 'Y' and user_input != 'y':
            print('Goodbye')
