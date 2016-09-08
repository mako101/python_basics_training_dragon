from random import randint

class Number(object):

    def __init__(self, min = 1, max = 99):

        # the minimum number to generate
        self.__min = min

        # the maximum number ot generate
        self.__max = max


    def gen_number(self, min = 1, max = 99):

        # polimorphism
        if min == 1 and max == 99:
            new_number = randint(self.__min, self.__max)

        else:
            new_number = randint(min, max)

        return new_number
