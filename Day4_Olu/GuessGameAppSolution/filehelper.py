
class FileHelper(object):

    __FILENAME = "settings.txt"

    @staticmethod
    def saveToFile(text):

        try:

            with open(FileHelper.__FILENAME, "w") as fw:

                #save the text
                fw.write(text)

        except:
            #I am saying nothing to the user because I want him or her to continue the game and not worry about this error
            #Highest I will do is send an email to myself about this error
            '''say nothing'''

    @staticmethod
    def readFromFile():

        try:

            with open(FileHelper.__FILENAME, "r") as fr:

                #return the content
                return fr.read()

        except:

            '''say nothing'''

