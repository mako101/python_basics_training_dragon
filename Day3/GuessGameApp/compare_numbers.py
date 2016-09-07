
class CompareNumbers(object):

    def __init__(self, first_number, second_number):
        self.__first_number = first_number
        self.__next_number = second_number

    def compare(self):
        if self.__next_number > self.__first_number:
            result = 'H'
        else:
            result = 'L'

        return result

