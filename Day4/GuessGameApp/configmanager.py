
class FileOps(object):

    __FILE = 'settings.txt'

    # find relevant config line and return its index
    @staticmethod
    def findLineIndex(item):

        lines = open(FileOps.__FILE, 'r+').readlines()

        for line in lines:
            if item in line:
                line_index = lines.index(line)

        return line_index

    # update file config for specified item
    @staticmethod
    def saveValue(item, value):
        try:
            # if the value exists:
            # update the line its in and overwrite the file
            try:
                lines = open(FileOps.__FILE, 'r').readlines()
                line_index = FileOps.findLineIndex(item)

                # update lines list
                lines[line_index] = str(item + ':' + str(value) + '\n')

                # write it to file
                with open(FileOps.__FILE, 'w') as out:
                    out.writelines(lines)

            # otherwise add a new line to the config file
            except:
                line = str(item + ':' + str(value) + '\n')
                with open(FileOps.__FILE, 'a') as out:
                    out.writelines(line)

        # general exception
        except:
            print('Could not save', item, '\n')

    # update file config for specified item
    @staticmethod
    def loadValue(item):
        try:
            lines = open(FileOps.__FILE, 'r').readlines()
            line_index = FileOps.findLineIndex(item)

            # get the value
            value = lines[line_index].split(':', 1)[1]
            # get rid of the newline
            value = value.strip()
            return value
        except:
            '''say nothing'''

#print(FileOps.findLineIndex('Lives'))
# FileOps.saveValue('Lives', 10)
# FileOps.saveValue('Score', 10)
# print(FileOps.loadValue('Lives'))

