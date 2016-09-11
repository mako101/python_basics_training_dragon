import configmanager


class Counter(object):

    # @staticmethod
    # def displayItems(item):
    #     return item

    @staticmethod
    def gainItem(item):
        item += 1

    @staticmethod
    def loseItem(item):
        item -= 1

    @staticmethod
    def resetItems(item, default):
        item = default

    # NOT NEEDED, can just call configmanager.FileOps.saveValue()
    # But can set it here so that its obivous
    @staticmethod
    def saveToFile(item_name, item):
        configmanager.FileOps.saveValue(item_name, item)

    @staticmethod
    def loadFromFile(item_name, default):

        # try to read the value from file or return default
        try:
            saved = configmanager.FileOps.loadValue(item_name)
            saved = int(saved)

        # use default value if there are any problems
        except:
            saved = default
        return saved

print(Counter.loadFromFile('Score', 0))
