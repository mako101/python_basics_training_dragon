import filehelper

class GameLife(object):

    __DEFAULTLIFE = 3

    __LIFE = __DEFAULTLIFE

    @staticmethod
    def getLife():

        return GameLife.__LIFE

    @staticmethod
    def resetLife():

        GameLife.__LIFE =  GameLife.__DEFAULTLIFE

    @staticmethod
    def increaseLife():

        GameLife.__LIFE += 1

    @staticmethod
    def decreaseLife():

        GameLife.__LIFE -= 1

    @staticmethod
    def setLifeFromFile():

        try:

            #read file content
            text = filehelper.FileHelper.readFromFile().split(":", 1)

            # print("Text is", text[1])

            GameLife.__LIFE = int(text[1])

        except:

            '''I do nothing'''

    @staticmethod
    def saveLifeToFile():

        filehelper.FileHelper.saveToFile("Life:" + str(GameLife.__LIFE))