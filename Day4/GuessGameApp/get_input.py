import game_session


class GetInput(object):

    __MSG = 'Please enter H for higher or L for Lower, Q to quit or N new game: '

    @staticmethod
    def user_choice():

        # this won't crash no matter which  characters the users type
        # so no need for exceptions
        user_input = input(GetInput.__MSG).upper()

        # Make sure only the right values can be passed
        while user_input != 'H' and user_input != 'L':
            if user_input == 'Q':
                game_session.GameSession.save_and_quit()
            elif user_input == 'N':
                game_session.GameSession.new_game()
            else:
                user_input = input(GetInput.__MSG).upper()

        return user_input
