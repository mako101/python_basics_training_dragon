

# this class decides whether user has guessed correctly
class GameLogic(object):

    # first the app compares numbers
    # then we compare the result with user input
    @staticmethod
    def decide(first_number, next_number, user_input):

        if next_number > first_number:
            result = 'H'
        else:
            result = 'L'

        if result == user_input:
            decision = 1
        else:
            decision = 0

        return decision
