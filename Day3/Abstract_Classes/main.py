# Abstract keyword is not supported in python, so we have to use this trick

# I want to force sub classes (i.e dog and cat) to have their own speak method, and get an error if they dont

import dog, cat

# the below will throw an error to show the class can't be instantiated
#anim = animal.Animal()



# all good here
dg = dog.Dog('Bingo')

dg.speak()


ct = cat.Cat('Fluffy')
ct.speak()