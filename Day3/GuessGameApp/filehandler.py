
file = 'test.txt'
item_name = 'Score'
item = 15

# find relevant config line and return its index
def findLineIndex(file, item_name):

    lines = open(file, 'r+').readlines()

    for line in lines:
        if item_name in line:
            line_index = lines.index(line)

    return line_index


# update file config for specified item
def updateConfigLine(file, item_name, item):

    try:
        lines = open(file, 'r+').readlines()

        line_index = findLineIndex(file, item_name)

        # construct line
        lines[line_index] = str(item_name + ':' + str(item) + '\n')

        out = open(file, 'w')
        out.writelines(lines)
        out.close()
    except:
        '''say nothing'''


# update file config for specified item
def readConfigLine(file, item_name):
    try:
        lines = open(file, 'r+').readlines()

        line_index = findLineIndex(file, item_name)

        line = lines[line_index]
        print(line)

        # construct line
        lines[line_index] = str(item_name + ':' + str(item) + '\n')

        out = open(file, 'w')
        out.writelines(lines)
        out.close()
    except Exception as e:
        print(e)
        '''say nothing'''

readConfigLine(file, item_name)


# updateConfigLine(file, item_name, item)


#
#
# lines[1] = str('Score' + ':' '20' + '\n')
# print(lines[1])
# print(lines)


#    f.writelines(lines)










# lines[line_num] = text
# out = open(file_name, 'w')
# out.writelines(lines)
# out.close()

