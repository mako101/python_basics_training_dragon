
class Game_Logic(object):

    def __init__(self, compare_result, user_input):
        self.__compare_result = compare_result
        self.__user_input = user_input

    def decide(self):
        if self.__compare_result == self.__user_input:
            result = 'You Win!'

        else:
            result = 'You lost'

        return result
