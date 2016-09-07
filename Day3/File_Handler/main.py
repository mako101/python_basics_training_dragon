
#  set is the list of unique elements
# similar to dictionary
# it is ordered
# it is fast when looping

population = set()
population.add(40)
population.add(30)
population.add(40)
population.add(50)
population.add(50)
population.add(30)

print(population)
# {40, 50, 30}



## Save population to a file
#  use open fucntion

# when using with, when it gets to the end, the 'f' variable is no more
# the memory is released and the file is closed, without using the close method

with open('example.txt', 'w') as f:

    f.write(str(population))

    # add new line
    f.write('\n')

    for item in population:

        #write to file
        f.write(str(item))

        # add new line
        f.write('\n')

    else:
        print('Writing finished')

# read from file
print()
print('Reading file')

with open('example.txt', 'r') as fr:

    line = fr.read(20)  # specify how many characters to read from the whole file

    # the operation above will move the cursor reading the file!
    # the next operation will be performed from where the cursor is
    # to reset it , need to use .seek method
    fr.seek(0) # resets to the start of the file
    line2 = fr.readline(10)  # specify how many characters to read from this line

    print(line)
    print()
    print(line2)
