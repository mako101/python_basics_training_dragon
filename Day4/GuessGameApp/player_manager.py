import counter as c
import game_session


class PlayerManager(object):

    def __init__(self, outcome, lives, score, next_number):

        self.__outcome = outcome
        self.__lives = lives
        self.__score = score
        self.__next_number = next_number

    def process_result(self):

        if self.__outcome == 1:
            print('You Win!')
            print("The second number was: ", self.__next_number)
            c.Counter.add('Lives', self.__lives)
            c.Counter.add('Score', self.__score)

        elif self.__outcome == 0:
            print('You Lost')
            print("The second number was: ", self.__next_number)
            c.Counter.substract('Lives', self.__lives)







