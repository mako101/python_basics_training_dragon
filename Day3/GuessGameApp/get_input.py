
class GetInput(object):

    def __init__(self, first_number):

        self.__first_number = first_number

    def get_input(self):

        print('The first number is', self.__first_number)

        user_input = input("Do you think my number is higher or lower?")

        # Make sure only the right values can be passed
        while user_input != 'H' and user_input != 'L':
                print('Please enter H for higher or L for Lower')
                # ASK OLU
                # Have to reset the variable again,
                # otherwise it will always have the furst value the user typed
                user_input = input("Do you think my number is higher or lower?")

        return user_input
