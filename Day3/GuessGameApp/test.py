
file = 'test.txt'
item_name = 'Score'
item = 10

# get the index of the relevant line
def updateConfigLine(file, item_name, item):
    f = open(file, 'r+')
    lines = f.readlines()
    #print(lines)

    for line in lines:
        if item_name in line:
            line_index = lines.index(line)

    # construct line
    lines[line_index] = str(item_name + ':' + str(item) + '\n')

    out = open(file, 'w')
    out.writelines(lines)

updateConfigLine(file, item_name, item)
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

