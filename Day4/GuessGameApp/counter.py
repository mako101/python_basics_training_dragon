import configmanager as c
import game_session

class Counter(object):

    @staticmethod
    def add(item, value):
        value += 1
        c.FileOps.save_value(item, value)

    @staticmethod
    def substract(item, value):
        value -= 1
        if value == 0:
            # Reset the game
            game_session.GameSession.game_over()
        else:
            c.FileOps.save_value(item, value)

    @staticmethod
    def load_from_file(item, default):

        # try to read the value from file or return default
        try:
            saved = c.FileOps.load_value(item)
            saved = int(saved)

        # use default value if there are any problems
        except:
            saved = default
        return saved

