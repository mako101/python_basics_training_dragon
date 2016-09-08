
class FileOps(object):

    # Capitals to indicate this is a 'constant' variable, ie not to be changed
    __FILE = 'settings.txt'

    @staticmethod
    def SaveToFile(data):

        try:
            with open(FileOps.__FILE, 'w') as save_file:
                # ensure that we write string data
                save_file.write(str(data))
        except:
            # We dont want to alert the user, so that they keep playing the game! -_-
            '''do nothing'''

    @staticmethod
    def LoadFromFile():

        try:
            with open(FileOps.__FILE, 'r') as load_file:
                # ensure that we read integer
                return int(load_file.read())
        except:
            '''do nothing'''


