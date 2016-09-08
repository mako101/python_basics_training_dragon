
class FileOps():

    def __init__(self, data='', file='settings.txt'):

        self.__file = file
        self._data = data


    def SaveToFile(self):
        with open(self.__file, 'w') as save_file:
            # ensure that we write string data
            save_file.write(str(self._data))


    def LoadFromFile(self):
        with open(self.__file, 'r') as save_file:
            # ensure that we read integer
            return int(save_file.read())