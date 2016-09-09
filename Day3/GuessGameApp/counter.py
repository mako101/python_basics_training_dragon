import file_io

class Counter(object):
    
    # # We set up the default amount of lives and set the lives to it if there not found in the file
    # __DEFAULT_ITEMS = 3
    #
    # # This is class variable, so it will be updated everywhere throughout the course of the game
    # # __ITEMS = __DEFAULT_ITEMS

    @staticmethod
    def displayItems(item):
        return item

    @staticmethod
    def gainItem(item):
        item += 1

    @staticmethod
    def loseItem(item):
        item -= 1

    @staticmethod
    def resetItems(item, default):
        item = default

    @staticmethod
    def saveItemsToFile(item_name, item):
        file_io.FileOps.SaveToFile(str(item_name) + ':' + str(item))

    @staticmethod
    def loadItemsFromFile():

        # we dont do anything here if exception is caught
        # This is so that the game can start without the settings file
        try:
            saved = file_io.FileOps.LoadFromFile().split(':')[1]
            saved = int(saved)
            print(saved)
            Counter.__ITEMS = saved
        except Exception as e:
            print(e)
            '''do nothing'''

Counter.loadLivesFromFile()