# Create a line breaker
print('*' * 50)

print("Tuples section")

# tuples are IMMUTABLE list of objects that cannot be changed

# 1st way to create a population tuple
pop_tuple = 40, 30, 60, 80, 50

# 2nd way
pop_tuple_second = (40, 30, 60, 80, 50)

# display
print('pop tuple is', pop_tuple, 'and is', type(pop_tuple))
print('pop tuple second is', pop_tuple_second, 'and is', type(pop_tuple_second))

#Can perform slicing/indexing just like with strings
print('The first item of the pop_tuple is ', pop_tuple[0])
print('The third item of the pop_tuple is ', pop_tuple[-3])
print('The third item of the pop_tuple to the end is ', pop_tuple[2:])
print('The third item of the pop_tuple to the end is ', pop_tuple[-3:])
print('The 2nd item of the pop_tuple to the 4th is ', pop_tuple[1:4])

print('''\nTuples are completely immutable!
You cannot change/add/delete/sort them!!!''')

# pop_tuple[2] = 40
# del pop_tuple[2]
# pop_tuple.append(30)

# empty line
print()
# Create a line breaker
print('*' * 50)
print("List section")

# You can do the same operations with lists
pop_list = [40, 30, 60, 80, 50]

# display
print('pop list is', pop_list, 'and is', type(pop_list))

#Can perform slicing/indexing just like with strings
print('The first item of the pop_list is ', pop_list[0])
print('The third item of the pop_list is ', pop_list[-3])
print('The third item of the pop_list to the end is ', pop_list[2:])
print('The third item of the pop_list to the end is ', pop_list[-3:])
print('The 2nd item of the pop_list to the 4th is ', pop_list[1:4])

# Modify element
pop_list[2] = 40

# display
print('pop list after change is', pop_list)

# delete element
del pop_list[2]

# display
print('pop list after deletion is', pop_list)

# Add new element
pop_list.append(75)

# display
print('pop list with nrew element is', pop_list)

# Insert new element (120) into the 3rd position in the list
pop_list.insert(2, 120)

# display
print('pop list with new 3rd element of 120 is', pop_list)


# Create a line breaker
print('*' * 50)

print("Dictionary section")

# key-pair values

pop_dictionary = {'London':40, 'Manchester':30, 'Southbank':60, 'Salisbury':80, 'Kent':50}

# display
print('pop_dictionary is', pop_dictionary)
print('The population of Londoin in the pop_dictionary is', pop_dictionary['London'])
# print('The population of London in the pop_dictionary is', pop_dictionary['Foo']) #throws KeyError

# Change the population in Manchester
pop_dictionary['Manchester'] = 400

# display
print('pop_dictionary is', pop_dictionary)

# Add a new value - same as above
# BEWARE - if you want to change the value that doesnt exist, it will be added instead!!
# If this is a problem, need to write separate logic to watch out for this
pop_dictionary['Briston'] = 35

# display
print('pop_dictionary is', pop_dictionary)

# print just keys or just values
print('pop_dictionary keys are', pop_dictionary.keys())
print('pop_dictionary values are', pop_dictionary.values())

# clear all items from the dict (also works with lists)
pop_dictionary.clear()
# display
print('pop_dictionary cleared is', pop_dictionary)

# delete the dictionary -> thiw removes it completely and it cannot be used anymore
del pop_dictionary

# # display
# print('pop_dictionary is', pop_dictionary)

# Create a line breaker
print('*' * 50)
print("Loops section")
# Create a line breaker
print('*' * 50)
print('For Loop')

#1st way
for item in pop_tuple:
    print('pop_tuple item is', item)

#this is an optional statement that ALWAYS runs!
else:
    print('\nFirst loop method is finished\n')


#2nd way - refrering to the item by index, also discovering the length of the list
for index in range(len(pop_tuple)):
    print('pop_tuple[%s] is %d' % (index, pop_tuple[index]))

#this is an optional statement that ALWAYS runs!
else:
    print('\nSecond loop method is finished\n')

# Create a line breaker
print('*' * 50)
print('While Loop')


# For while loop you need 2 things:
# The condition to initialize it and the incrementation/count to stop it, otherwise it will be an infinite loop

count = 0

while count < len(pop_tuple):
    print('pop_tuple[%s] is %d' % (count, pop_tuple[count]))

    # increment our counter
    count += 1

# Create a line breaker
print('*' * 50)
print('Exercise')

print(pop_tuple)

# Find minimum, maximum, total and average without using any statistics functions

# Solution - we compare evetyhing to one element of the tuple!!

# we start with the first element
minimum = pop_tuple[0]
maximum = pop_tuple[0]
total = pop_tuple[0]

# then perform the rest of operations against the remaining elements in the array

for index in range(1, len(pop_tuple)):

    # find minimum
    if pop_tuple[index] < minimum:
        minimum = pop_tuple[index]
        print('setting min to', minimum)

    # find maximum
    if pop_tuple[index] > maximum:
        maximum = pop_tuple[index]
        print('setting max to', maximum)

    total += pop_tuple[index]

average = total / len(pop_tuple)


# Display results:
print()
print('The minimum is', minimum)
print('The maximum is', maximum)
print('The total is', total)
print('The average is', average)