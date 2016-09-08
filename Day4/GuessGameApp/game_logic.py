
# this class decides whether users answer matches app's answer
class GameLogic(object):

    def __init__(self, compare_result, user_input):

        self.__compare_result = compare_result
        self.__user_input = user_input

    def decide(self):
        if self.__compare_result == self.__user_input:
            result = 1

        else:
            result = 0

        return result
